from io import StringIO

import pytest
from django.core.management import call_command

import cuhasc.constants as c
import cuhasc.deployment as deployment
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


# ---- AdminPage singleton ----

def test_adminpage_current_creates_the_singleton_once(db):
    first = AdminPage.current()
    assert AdminPage.objects.count() == 1
    assert len(first.token) == c.TOKEN_LENGTH_ADMINPAGE
    again = AdminPage.current()
    assert AdminPage.objects.count() == 1
    assert again.token == first.token, \
        "current() must not rotate: it runs at every server start, and a new token would " \
        "invalidate the link the Culture Lead saved"


def test_adminpage_reset_rotates_the_token_without_adding_instances(db):
    first = AdminPage.current().token
    rotated = AdminPage.reset()
    assert AdminPage.objects.count() == 1
    assert rotated.token != first
    assert AdminPage.objects.get().token == rotated.token, "must be saved, not just in memory"


def test_adminpage_reset_also_works_on_an_empty_database(db):
    assert AdminPage.objects.count() == 0
    AdminPage.reset()
    assert AdminPage.objects.count() == 1


# ---- adminpage management command ----

def _run_adminpage_command(*args) -> str:
    out = StringIO()
    call_command('adminpage', *args, stdout=out)
    return out.getvalue().strip()


def test_adminpage_command_creates_singleton_and_prints_link(db):
    link = _run_adminpage_command()
    assert AdminPage.objects.count() == 1
    token = AdminPage.objects.get().token
    assert link == f'http://localhost:8037/adminpage/{token}', \
        "the default must match where `cuhasc run` actually listens"


def test_adminpage_command_resets_token_without_adding_instances(db):
    _run_adminpage_command()
    first = AdminPage.objects.get().token
    _run_adminpage_command()
    assert AdminPage.objects.count() == 1            # still one instance
    assert AdminPage.objects.get().token != first    # token refreshed


def test_adminpage_command_uses_the_base_url_it_is_given(db, monkeypatch):
    # Behind a tunnel the printed link is useless unless it carries the public URL.
    link = _run_adminpage_command('--base-url', 'https://x.trycloudflare.com/')
    assert link == f'https://x.trycloudflare.com/adminpage/{AdminPage.objects.get().token}'
    monkeypatch.setenv(deployment.PUBLIC_URL_ENV, 'https://from-environment.example')
    link = _run_adminpage_command()
    assert link.startswith('https://from-environment.example/adminpage/')
