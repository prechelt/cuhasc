import json

import pytest
from django.urls import reverse

import cuhasc.constants as c
import cuhasc.handbook as handbook
import cuhasc.instruments as instruments
from cuhasc.models import AdminPage, Member, QResult, Team


@pytest.fixture
def member(db):
    team = Team.objects.create(name='TestTeam', token='TEAMTOKEN1')
    return Member.objects.create(name='Alice', token='MEMBERTKN1', team=team)


@pytest.fixture
def team(db):
    return Team.objects.create(name='TestTeam', token='TEAMTOKEN1', member_token='MBRTOKEN01')


def _full_answers(language='en'):
    """A complete, valid set of answers (every item -> '3') for the questionnaire."""
    return {item.item: '3' for item in instruments.get_questionnaire(language)}


def test_show_member_requires_correct_token(client, member):
    assert client.get(reverse('show_member', args=[member.id, 'wrongtoken'])).status_code == 404
    assert client.get(reverse('show_member', args=[member.id, member.token])).status_code == 200


def test_show_member_renders_culture_profile_svg(client, member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=3)
    QResult.objects.create(member=member, item='PO2', scale='disagree5', value=5)
    content = client.get(reverse('show_member', args=[member.id, member.token])).content.decode()
    assert '<svg' in content
    assert 'Power Distance' in content       # localized label, default language en
    assert content.count('<circle') == 1     # one dot for the single defined Score (PO)


def test_show_member_has_no_dots_without_answers(client, member):
    content = client.get(reverse('show_member', args=[member.id, member.token])).content.decode()
    assert content.count('<circle') == 0


# ---- show_team Team Culture Profile rendering ----

def _answer(member, item, value):
    QResult.objects.create(member=member, item=item, scale='disagree5', value=value)


@pytest.fixture
def team_with_answers(db):
    team = Team.objects.create(name='TestTeam', token='TEAMTOKEN1')
    alice = Member.objects.create(name='Alice', token='ALICETKN03', team=team)
    bob = Member.objects.create(name='Bob', token='BOBTOKEN03', team=team)
    _answer(alice, 'PO1', 4)
    _answer(bob, 'PO1', 2)
    return team


def test_show_team_requires_correct_token(client, team_with_answers):
    url = reverse('show_team', args=[team_with_answers.id, 'wrongtoken'])
    assert client.get(url).status_code == 404


def test_show_team_accessible_with_correct_token(client, team_with_answers):
    url = reverse('show_team', args=[team_with_answers.id, team_with_answers.token])
    assert client.get(url).status_code == 200


def test_show_team_renders_member_and_mean_dots(client, team_with_answers):
    url = reverse('show_team', args=[team_with_answers.id, team_with_answers.token])
    content = client.get(url).content.decode()
    assert '<svg' in content
    assert content.count('class="member-dot"') == 2   # one small dot per member on PO
    assert content.count('class="mean-dot"') == 1      # one larger team-mean dot on PO


def test_show_team_no_svg_when_no_answers(client, db):
    team = Team.objects.create(name='Empty', token='TEAMTOKEN2')
    Member.objects.create(name='Empty', token='EMPTYTKN02', team=team)
    url = reverse('show_team', args=[team.id, team.token])
    content = client.get(url).content.decode()
    assert '<svg' not in content


def test_show_team_member_labels_hidden_by_default(client, team_with_answers):
    url = reverse('show_team', args=[team_with_answers.id, team_with_answers.token])
    content = client.get(url).content.decode()
    assert 'class="member-label"' in content
    assert 'visibility="hidden"' in content
    assert 'type="checkbox"' in content


# ---- show_team matching-Section list grouped by Chapter (issue #11) ----

def write_section(tmp_path, filename: str, title: str = "A Title",
                   trigger: str = "one-high(PO)", body: str = "Some body text.\n"):
    path = tmp_path / filename
    path.write_text(f"---\ntitle: {title}\ntrigger: {trigger}\n---\n{body}")
    return path


def test_show_team_lists_matching_section_grouped_by_chapter(client, team_with_answers, tmp_path):
    # Alice=4, Bob=2 on PO: one-high(PO) matches, one-low(PO) matches too.
    write_section(tmp_path, "dailystandup-a.md", title="Speak Up", trigger="one-high(PO)")
    handbook.load_sections(str(tmp_path / '*.md'))
    url = reverse('show_team', args=[team_with_answers.id, team_with_answers.token])
    content = client.get(url).content.decode()
    assert 'dailystandup' in content
    assert 'Speak Up' in content
    assert reverse('handbook_section', args=["dailystandup-a"]) in content


def test_show_team_omits_non_matching_section(client, team_with_answers, tmp_path):
    # no UN answers at all: no Predicate on UN can be true.
    write_section(tmp_path, "dailystandup-a.md", title="Speak Up", trigger="one-high(UN)")
    handbook.load_sections(str(tmp_path / '*.md'))
    url = reverse('show_team', args=[team_with_answers.id, team_with_answers.token])
    content = client.get(url).content.decode()
    assert 'Speak Up' not in content


def test_show_team_no_section_list_without_team_culture_profile(client, db, tmp_path):
    write_section(tmp_path, "dailystandup-a.md", title="Speak Up", trigger="one-high(PO)")
    handbook.load_sections(str(tmp_path / '*.md'))
    team = Team.objects.create(name='Empty', token='TEAMTOKEN3')
    Member.objects.create(name='Empty', token='EMPTYTKN03', team=team)  # no answers
    url = reverse('show_team', args=[team.id, team.token])
    content = client.get(url).content.decode()
    assert 'Speak Up' not in content
    assert '<h2>Handbook</h2>' not in content


# ---- questionnaire language selector + switch-vs-submit (issue #4) ----

def _cookie_language(client):
    morsel = client.cookies.get(c.COOKIE_NAME)
    return json.loads(morsel.value).get('language') if morsel else None


def test_create_member_shows_language_dropdown(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    content = client.get(url).content.decode()
    assert 'dropdown-menu' in content                       # Bootstrap dropdown, not <select>
    assert 'name="switch_language"' in content
    assert 'Deutsch' in content and 'German' in content     # English name | autonym row


def test_edit_member_shows_language_dropdown(client, member):
    url = reverse('edit_member', args=[member.id, member.token])
    content = client.get(url).content.decode()
    assert 'dropdown-menu' in content
    assert 'name="switch_language"' in content


def test_create_member_language_switch_preserves_answers_without_errors(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    data = {'name': 'Alice', 'PO1': '4', 'switch_language': 'de'}
    resp = client.post(url, data)
    assert resp.status_code == 200                           # re-render, no redirect
    content = resp.content.decode()
    assert 'stimme überhaupt nicht zu' in content            # German scale labels -> switched
    assert 'value="4"\n' not in content or 'checked' in content
    assert 'checked' in content                              # the entered PO1=4 stays selected
    assert 'errorlist' not in content                        # a switch surfaces no errors
    assert Member.objects.count() == 0                       # nothing saved on a switch


def test_create_member_language_switch_sets_cookie(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    client.post(url, {'name': '', 'switch_language': 'de'})
    assert _cookie_language(client) == 'de'


def test_create_member_real_submit_saves_qresults(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    data = {'name': 'Alice', **_full_answers('en')}
    resp = client.post(url, data)
    assert resp.status_code == 302                           # redirect on successful save
    member = Member.objects.get(name='Alice')
    assert member.qresults.count() == len(_full_answers('en'))


def test_edit_member_language_switch_preserves_answers_without_errors(client, member):
    url = reverse('edit_member', args=[member.id, member.token])
    resp = client.post(url, {'name': 'Alice', 'PO1': '2', 'switch_language': 'de'})
    assert resp.status_code == 200
    content = resp.content.decode()
    assert 'stimme überhaupt nicht zu' in content
    assert 'errorlist' not in content
    assert member.qresults.count() == 0                      # not saved on a switch


def test_create_member_initial_render_uses_cookie_language(client, team):
    client.cookies[c.COOKIE_NAME] = json.dumps({'roles': [], 'language': 'de'})
    url = reverse('create_member', args=[team.id, team.member_token])
    content = client.get(url).content.decode()
    assert 'stimme überhaupt nicht zu' in content            # German because cookie says 'de'


def test_create_member_initial_render_uses_accept_language_without_cookie(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    content = client.get(url, HTTP_ACCEPT_LANGUAGE='de').content.decode()
    assert 'stimme überhaupt nicht zu' in content            # German from Accept-Language header


def test_create_member_accept_language_picks_first_supported_tag(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    # 'xx' is not a cuhasc language and is preferred (q=1.0 by default) over 'de' (q=0.5)
    content = client.get(url, HTTP_ACCEPT_LANGUAGE='xx,de;q=0.5').content.decode()
    assert 'stimme überhaupt nicht zu' in content


def test_create_member_cookie_language_wins_over_accept_language(client, team):
    client.cookies[c.COOKIE_NAME] = json.dumps({'roles': [], 'language': 'en'})
    url = reverse('create_member', args=[team.id, team.member_token])
    content = client.get(url, HTTP_ACCEPT_LANGUAGE='de').content.decode()
    assert 'strongly disagree' in content                   # cookie's 'en' wins over header's 'de'


def test_create_member_initial_render_defaults_to_english_without_cookie_or_header(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    content = client.get(url).content.decode()
    assert 'strongly disagree' in content


# ---- adminpage: recover Team/Member links if the cookie is lost ----

def test_adminpage_requires_correct_token(client, db):
    AdminPage.objects.create(token='ADMINTKN01')
    assert client.get(reverse('adminpage', args=['wrongtoken'])).status_code == 404
    assert client.get(reverse('adminpage', args=['ADMINTKN01'])).status_code == 200


def test_adminpage_lists_teams_and_members(client, member):
    AdminPage.objects.create(token='ADMINTKN01')
    content = client.get(reverse('adminpage', args=['ADMINTKN01'])).content.decode()
    assert 'Teams and members' in content
    assert reverse('show_team', args=[member.team.id, member.team.token]) in content
    assert reverse('edit_team', args=[member.team.id, member.team.token]) in content
    assert reverse('create_member', args=[member.team.id, member.team.member_token]) in content
    assert reverse('show_member', args=[member.id, member.token]) in content
    assert reverse('edit_member', args=[member.id, member.token]) in content
    assert 'Alice' in content
