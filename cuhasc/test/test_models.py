import pytest

from cuhasc.models import Member, QResult, Team


@pytest.fixture
def member(db):
    team = Team.objects.create(name='TestTeam', token='TEAMTOKEN1')
    return Member.objects.create(name='Alice', token='MEMBERTKN1', team=team)


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
