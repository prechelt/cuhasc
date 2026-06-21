import pytest
from django.urls import reverse

import cuhasc.instruments as instruments
from cuhasc.models import Member, QResult, Team


# ---- dimension name loader tests ----

def test_get_dimension_name_en_power_distance():
    assert instruments.get_dimension_name('PO', 'en') == 'Power Distance'


def test_get_dimension_name_de_power_distance():
    assert instruments.get_dimension_name('PO', 'de') == 'Machtdistanz'


def test_get_dimension_name_en_all_five():
    codes = ['PO', 'UN', 'CO', 'LT', 'MA']
    for code in codes:
        name = instruments.get_dimension_name(code, 'en')
        assert isinstance(name, str) and len(name) > 0, f"No EN name for {code}"


def test_get_dimension_name_de_all_five():
    codes = ['PO', 'UN', 'CO', 'LT', 'MA']
    for code in codes:
        name = instruments.get_dimension_name(code, 'de')
        assert isinstance(name, str) and len(name) > 0, f"No DE name for {code}"


# ---- Member.culture_profile() tests ----

@pytest.fixture
def team(db):
    return Team.objects.create(name='TestTeam', token='TEAMTOKEN1')


@pytest.fixture
def member(team):
    return Member.objects.create(name='Alice', token='MEMBERTKN1', team=team)


def test_culture_profile_empty(member):
    profile = member.culture_profile()
    assert profile == {}


def test_culture_profile_single_dimension(member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=3)
    QResult.objects.create(member=member, item='PO2', scale='disagree5', value=5)
    profile = member.culture_profile()
    assert 'PO' in profile
    assert profile['PO'] == pytest.approx(4.0)


def test_culture_profile_mean_of_present_values(member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=2)
    QResult.objects.create(member=member, item='PO2', scale='disagree5', value=4)
    QResult.objects.create(member=member, item='PO3', scale='disagree5', value=3)
    profile = member.culture_profile()
    assert profile['PO'] == pytest.approx(3.0)


def test_culture_profile_dimension_with_no_answers_excluded(member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=3)
    profile = member.culture_profile()
    assert 'PO' in profile
    assert 'UN' not in profile
    assert 'CO' not in profile


def test_culture_profile_multiple_dimensions(member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=4)
    QResult.objects.create(member=member, item='UN1', scale='important5', value=2)
    profile = member.culture_profile()
    assert profile['PO'] == pytest.approx(4.0)
    assert profile['UN'] == pytest.approx(2.0)


# ---- Team.culture_profile() tests ----

def _answer(member, item, value):
    QResult.objects.create(member=member, item=item, scale='disagree5', value=value)


def test_team_culture_profile_ok(team):
    alice = Member.objects.create(name='Alice', token='ALICETKN01', team=team)
    bob = Member.objects.create(name='Bob', token='BOBTOKEN01', team=team)
    _answer(alice, 'PO1', 4)
    _answer(alice, 'UN1', 5)
    _answer(bob, 'PO1', 2)
    result = team.culture_profile()
    names = {m['name']: m['profile'] for m in result['members']}
    assert names['Alice']['PO'] == pytest.approx(4.0)
    assert names['Bob']['PO'] == pytest.approx(2.0)
    # per-Dimension team mean
    assert result['means']['PO'] == pytest.approx(3.0)   # (4 + 2) / 2
    assert result['means']['UN'] == pytest.approx(5.0)   # only Alice answered UN


def test_team_culture_profile_omits_zero_answer_members(team):
    alice = Member.objects.create(name='Alice', token='ALICETKN02', team=team)
    Member.objects.create(name='Empty', token='EMPTYTKN01', team=team)  # no answers
    _answer(alice, 'PO1', 3)
    result = team.culture_profile()
    names = [m['name'] for m in result['members']]
    assert names == ['Alice']
    assert result['means']['PO'] == pytest.approx(3.0)


# ---- show_team SVG rendering tests ----

@pytest.fixture
def team_with_answers(team):
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


def test_show_team_no_svg_when_no_answers(client, team):
    Member.objects.create(name='Empty', token='EMPTYTKN02', team=team)
    url = reverse('show_team', args=[team.id, team.token])
    content = client.get(url).content.decode()
    assert '<svg' not in content


def test_show_team_member_labels_hidden_by_default(client, team_with_answers):
    url = reverse('show_team', args=[team_with_answers.id, team_with_answers.token])
    content = client.get(url).content.decode()
    # labels exist but are hidden, and a checkbox toggles them
    assert 'class="member-label"' in content
    assert 'visibility="hidden"' in content
    assert 'type="checkbox"' in content


# ---- show_member SVG rendering tests ----

def test_show_member_requires_correct_token(client, member):
    url = reverse('show_member', args=[member.id, 'wrongtoken'])
    response = client.get(url)
    assert response.status_code == 404


def test_show_member_accessible_with_correct_token(client, member):
    url = reverse('show_member', args=[member.id, member.token])
    response = client.get(url)
    assert response.status_code == 200


def test_show_member_contains_svg_when_answers_present(client, member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=3)
    url = reverse('show_member', args=[member.id, member.token])
    response = client.get(url)
    content = response.content.decode()
    assert '<svg' in content


def test_show_member_no_svg_when_no_answers(client, member):
    url = reverse('show_member', args=[member.id, member.token])
    response = client.get(url)
    content = response.content.decode()
    assert '<svg' not in content


def test_show_member_svg_has_dimension_label(client, member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=3)
    url = reverse('show_member', args=[member.id, member.token])
    response = client.get(url)
    content = response.content.decode()
    assert 'Power Distance' in content


def test_show_member_svg_has_dot_for_answered_dimension(client, member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=3)
    url = reverse('show_member', args=[member.id, member.token])
    response = client.get(url)
    content = response.content.decode()
    assert '<circle' in content


def test_show_member_svg_no_dot_for_unanswered_dimension(client, member):
    # Only PO has answers; the SVG should have exactly one circle
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=3)
    url = reverse('show_member', args=[member.id, member.token])
    response = client.get(url)
    content = response.content.decode()
    assert content.count('<circle') == 1
