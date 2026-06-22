import pytest
from django.urls import reverse

from cuhasc.models import Member, QResult, Team


@pytest.fixture
def member(db):
    team = Team.objects.create(name='TestTeam', token='TEAMTOKEN1')
    return Member.objects.create(name='Alice', token='MEMBERTKN1', team=team)


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
