from io import StringIO

import pytest
from django.core.management import call_command

from cuhasc.models import AdminPage, Member, QResult, Team


@pytest.fixture
def member(db):
    team = Team.objects.create(name='TestTeam', token='TEAMTOKEN1')
    return Member.objects.create(name='Alice', token='MEMBERTKN1', team=team)


@pytest.fixture
def team(db):
    return Team.objects.create(name='TestTeam', token='TEAMTOKEN1')


def _answer(member, item, value):
    QResult.objects.create(member=member, item=item, scale='disagree5', value=value)


def test_culture_profile_ok(member):
    # no answers: every Dimension undefined -> empty profile
    assert member.culture_profile() == {}
    # a Score is the mean of the present answers for that Dimension
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=2)
    QResult.objects.create(member=member, item='PO2', scale='disagree5', value=4)
    QResult.objects.create(member=member, item='PO3', scale='disagree5', value=3)
    QResult.objects.create(member=member, item='UN1', scale='disagree5', value=5)
    profile = member.culture_profile()
    assert profile['PO'] == pytest.approx(3.0)
    assert profile['UN'] == pytest.approx(5.0)


def test_culture_profile_excludes_dimension_with_no_answers(member):
    QResult.objects.create(member=member, item='PO1', scale='disagree5', value=3)
    profile = member.culture_profile()
    assert 'PO' in profile
    for code in ['UN', 'CO', 'LT', 'MA']:
        assert code not in profile


def test_team_culture_profile_per_member_and_mean(team):
    alice = Member.objects.create(name='Alice', token='ALICETKN01', team=team)
    bob = Member.objects.create(name='Bob', token='BOBTOKEN01', team=team)
    _answer(alice, 'PO1', 4)
    _answer(alice, 'UN1', 5)
    _answer(bob, 'PO1', 2)
    result = team.culture_profile()
    profiles = {m['name']: m['profile'] for m in result['members']}
    assert profiles['Alice']['PO'] == pytest.approx(4.0)
    assert profiles['Bob']['PO'] == pytest.approx(2.0)
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


# ---- cuhasc-adminpage management command ----

def _run_adminpage_command() -> str:
    out = StringIO()
    call_command('cuhasc-adminpage', stdout=out)
    return out.getvalue().strip()


def test_adminpage_command_creates_singleton_and_prints_link(db):
    link = _run_adminpage_command()
    assert AdminPage.objects.count() == 1
    token = AdminPage.objects.get().token
    assert link.endswith(f'/adminpage/{token}')


def test_adminpage_command_resets_token_without_adding_instances(db):
    _run_adminpage_command()
    first = AdminPage.objects.get().token
    _run_adminpage_command()
    assert AdminPage.objects.count() == 1            # still one instance
    assert AdminPage.objects.get().token != first    # token refreshed
