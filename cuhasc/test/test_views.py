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
