import pytest

import cuhasc.triggers as triggers


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
    # one-high: at least one Member at or above the high cutoff
    assert not triggers.evaluate('one-high(PO)', lowish)
    assert triggers.evaluate('one-high(PO)', mixed)
    assert triggers.evaluate('one-high(PO)', highish)
    # all-low: every Member at or below the low cutoff
    assert triggers.evaluate('all-low(PO)', lowish)
    assert not triggers.evaluate('all-low(PO)', mixed)
    assert not triggers.evaluate('all-low(PO)', highish)
    # mean-high / mean-low: the team mean against the same cutoffs
    assert not triggers.evaluate('mean-high(PO)', lowish)   # mean 1.5
    assert triggers.evaluate('mean-low(PO)', lowish)
    assert not triggers.evaluate('mean-high(PO)', mixed)    # mean 2.5
    assert not triggers.evaluate('mean-low(PO)', mixed)
    assert triggers.evaluate('mean-high(PO)', highish)      # mean 4.75
    assert not triggers.evaluate('mean-low(PO)', highish)
    # every Dimension code is usable
    for dim in ['PO', 'UN', 'CO', 'LT', 'MA']:
        assert triggers.evaluate(f"one-high({dim})", profile_of({dim: 5.0}))


def test_evaluate_at_the_cutoffs():
    """The cutoffs are inclusive on both sides."""
    assert triggers.evaluate('one-high(PO)', profile_of({'PO': triggers.HIGH_CUTOFF}))
    assert not triggers.evaluate('one-high(PO)', profile_of({'PO': triggers.HIGH_CUTOFF - 0.1}))
    assert triggers.evaluate('all-low(PO)', profile_of({'PO': triggers.LOW_CUTOFF}))
    assert not triggers.evaluate('all-low(PO)', profile_of({'PO': triggers.LOW_CUTOFF + 0.1}))
    assert triggers.evaluate('mean-high(PO)', profile_of({'PO': triggers.HIGH_CUTOFF}))
    assert triggers.evaluate('mean-low(PO)', profile_of({'PO': triggers.LOW_CUTOFF}))


def test_evaluate_ignores_members_lacking_the_dimension():
    """A Member without a Score for the Dimension neither satisfies nor blocks a Predicate."""
    assert triggers.evaluate('one-high(PO)', profile_of({'UN': 5.0}, {'PO': 5.0}))
    assert not triggers.evaluate('one-high(PO)', profile_of({'UN': 5.0}))
    assert triggers.evaluate('all-low(PO)', profile_of({'UN': 5.0}, {'PO': 1.0}))
    # a Dimension nobody answered has no mean to compare against
    assert not triggers.evaluate('mean-high(PO)', profile_of({'UN': 5.0}))
    assert not triggers.evaluate('mean-low(PO)', profile_of({'UN': 5.0}))


def test_evaluate_error():
    with pytest.raises(triggers.TriggerError, match='sometimes-high'):
        triggers.evaluate('sometimes-high(PO)', profile_of({'PO': 5.0}))
    with pytest.raises(triggers.TriggerError, match='XY'):
        triggers.evaluate('one-high(XY)', profile_of({'PO': 5.0}))
    for malformed in ['one-high', 'one-high(PO', 'one-high(PO))', 'one-high(PO) and all-low(UN)',
                      'one-high()', '', 'one_high(PO)', 'one-high(PO) ']:
        with pytest.raises(triggers.TriggerError, match='trigger'):
            triggers.evaluate(malformed, profile_of({'PO': 5.0}))


def test_registry_maps_the_four_fixed_predicate_names():
    assert sorted(triggers.PREDICATES) == ['all-low', 'mean-high', 'mean-low', 'one-high']
    for name, predicate in triggers.PREDICATES.items():
        assert predicate(profile_of({'PO': 3.0}), 'PO') in (True, False), f"{name} must return a bool"
