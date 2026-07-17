import pytest

import cuhasc.handbook as handbook
import cuhasc.instruments as instruments


def profile_of(*scores: dict) -> dict:
    """Team Culture Profile of one Member per given Culture Profile, plus the per-Dimension means."""
    members = [{'name': f"M{i}", 'profile': profile} for i, profile in enumerate(scores)]
    means = {}
    for dim in {dim for m in members for dim in m['profile']}:
        values = [m['profile'][dim] for m in members if dim in m['profile']]
        means[dim] = sum(values) / len(values)
    return {'members': members, 'means': means}


def test_evaluate_ok():
    lowish = profile_of({'PO': 1.0}, {'PO': 2.0})
    mixed = profile_of({'PO': 1.0}, {'PO': 4.0})
    highish = profile_of({'PO': 4.5}, {'PO': 5.0})
    # one-high / two-high: at least one resp. two Members at or above the high cutoff
    assert not handbook.evaluate('one-high(PO)', lowish)
    assert handbook.evaluate('one-high(PO)', mixed)
    assert handbook.evaluate('one-high(PO)', highish)
    assert not handbook.evaluate('two-high(PO)', lowish)
    assert not handbook.evaluate('two-high(PO)', mixed)  # only one Member is high
    assert handbook.evaluate('two-high(PO)', highish)
    # one-low / two-low: at least one resp. two Members at or below the low cutoff
    assert handbook.evaluate('one-low(PO)', lowish)
    assert handbook.evaluate('one-low(PO)', mixed)
    assert not handbook.evaluate('one-low(PO)', highish)
    assert handbook.evaluate('two-low(PO)', lowish)
    assert not handbook.evaluate('two-low(PO)', mixed)  # only one Member is low
    assert not handbook.evaluate('two-low(PO)', highish)
    # mean-high / mean-low: the team mean against the same cutoffs
    assert not handbook.evaluate('mean-high(PO)', lowish)   # mean 1.5
    assert handbook.evaluate('mean-low(PO)', lowish)
    assert not handbook.evaluate('mean-high(PO)', mixed)    # mean 2.5
    assert not handbook.evaluate('mean-low(PO)', mixed)
    assert handbook.evaluate('mean-high(PO)', highish)      # mean 4.75
    assert not handbook.evaluate('mean-low(PO)', highish)
    # every Dimension code is usable
    for dim in instruments.DIMENSIONS:
        assert handbook.evaluate(f"one-high({dim})", profile_of({dim: 5.0}))


def test_evaluate_at_the_cutoffs():
    """The cutoffs are inclusive on both sides."""
    assert handbook.evaluate('one-high(PO)', profile_of({'PO': handbook.HIGH_CUTOFF}))
    assert not handbook.evaluate('one-high(PO)', profile_of({'PO': handbook.HIGH_CUTOFF - 0.1}))
    assert handbook.evaluate('one-low(PO)', profile_of({'PO': handbook.LOW_CUTOFF}))
    assert not handbook.evaluate('one-low(PO)', profile_of({'PO': handbook.LOW_CUTOFF + 0.1}))
    assert handbook.evaluate('mean-high(PO)', profile_of({'PO': handbook.HIGH_CUTOFF}))
    assert handbook.evaluate('mean-low(PO)', profile_of({'PO': handbook.LOW_CUTOFF}))


def test_evaluate_ignores_members_lacking_the_dimension():
    """A Member without a Score for the Dimension neither satisfies nor blocks a Predicate."""
    assert handbook.evaluate('one-high(PO)', profile_of({'UN': 5.0}, {'PO': 5.0}))
    assert not handbook.evaluate('one-high(PO)', profile_of({'UN': 5.0}))
    assert handbook.evaluate('one-low(PO)', profile_of({'UN': 5.0}, {'PO': 1.0}))
    assert not handbook.evaluate('two-low(PO)', profile_of({'UN': 1.0}, {'PO': 1.0}))
    # a Dimension nobody answered has no mean to compare against
    assert not handbook.evaluate('mean-high(PO)', profile_of({'UN': 5.0}))
    assert not handbook.evaluate('mean-low(PO)', profile_of({'UN': 5.0}))


def test_evaluate_error():
    with pytest.raises(handbook.TriggerError, match='sometimes-high'):
        handbook.evaluate('sometimes-high(PO)', profile_of({'PO': 5.0}))
    with pytest.raises(handbook.TriggerError, match='all-low'):  # a Predicate that no longer exists
        handbook.evaluate('all-low(PO)', profile_of({'PO': 5.0}))
    with pytest.raises(handbook.TriggerError, match='XY'):
        handbook.evaluate('one-high(XY)', profile_of({'PO': 5.0}))
    for malformed in ['one-high', 'one-high(PO', 'one-high(PO))', 'one-high(PO) and two-low(UN)',
                      'one-high()', '', 'one_high(PO)', 'one-high(PO) ']:
        with pytest.raises(handbook.TriggerError, match='trigger'):
            handbook.evaluate(malformed, profile_of({'PO': 5.0}))


def test_registry_maps_the_six_fixed_predicate_names():
    assert sorted(handbook.PREDICATES) == ['mean-high', 'mean-low', 'one-high', 'one-low',
                                           'two-high', 'two-low']
    for name, predicate in handbook.PREDICATES.items():
        assert predicate(profile_of({'PO': 3.0}), 'PO') in (True, False), f"{name} must return a bool"
