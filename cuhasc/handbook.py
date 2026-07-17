"""Trigger parsing and Predicate evaluation for the Handbook.

A Trigger is a single Predicate call of the fixed shape ``predicate-name(DIMENSION)``,
e.g. ``one-high(PO)``, evaluated against a Team Culture Profile as produced by
``Team.culture_profile()``.
"""

import re

import cuhasc.instruments as instruments

HIGH_CUTOFF: float = 4.0  # a Score at or above this is "high"
LOW_CUTOFF: float = 2.0   # a Score at or below this is "low"

TRIGGER_REGEXP = re.compile(r"^([a-z]+(?:-[a-z]+)*)\(([A-Za-z]+)\)$")


class TriggerError(ValueError):
    """An invalid Trigger. Its message is shown verbatim by the Handbook loader."""


def member_scores(team_profile: dict, dimension: str) -> list[float]:
    """The Scores for one Dimension of those Members who have one."""
    return [member['profile'][dimension] for member in team_profile['members']
            if dimension in member['profile']]


def count_high(team_profile: dict, dimension: str) -> int:
    return sum(1 for score in member_scores(team_profile, dimension) if score >= HIGH_CUTOFF)


def count_low(team_profile: dict, dimension: str) -> int:
    return sum(1 for score in member_scores(team_profile, dimension) if score <= LOW_CUTOFF)


def one_high(team_profile: dict, dimension: str) -> bool:
    return count_high(team_profile, dimension) >= 1


def two_high(team_profile: dict, dimension: str) -> bool:
    return count_high(team_profile, dimension) >= 2


def one_low(team_profile: dict, dimension: str) -> bool:
    return count_low(team_profile, dimension) >= 1


def two_low(team_profile: dict, dimension: str) -> bool:
    return count_low(team_profile, dimension) >= 2


def mean_high(team_profile: dict, dimension: str) -> bool:
    mean = team_profile['means'].get(dimension)
    return mean is not None and mean >= HIGH_CUTOFF


def mean_low(team_profile: dict, dimension: str) -> bool:
    mean = team_profile['means'].get(dimension)
    return mean is not None and mean <= LOW_CUTOFF


PREDICATES: dict = {  # Predicate name -> callable(team_profile, dimension) -> bool
    'one-high': one_high,
    'two-high': two_high,
    'one-low': one_low,
    'two-low': two_low,
    'mean-high': mean_high,
    'mean-low': mean_low,
}


def evaluate(trigger: str, team_profile: dict) -> bool:
    """Whether the Section carrying this Trigger applies to this Team Culture Profile."""
    match = TRIGGER_REGEXP.match(trigger)
    if not match:
        raise TriggerError(f"malformed trigger '{trigger}': expected the form 'predicate-name(DIMENSION)'")
    name, dimension = match.group(1), match.group(2)
    if name not in PREDICATES:
        raise TriggerError(f"unknown predicate '{name}' in trigger '{trigger}': "
                           f"known predicates are {', '.join(sorted(PREDICATES))}")
    if dimension not in instruments.DIMENSIONS:
        raise TriggerError(f"unknown dimension '{dimension}' in trigger '{trigger}': "
                           f"known dimensions are {', '.join(instruments.DIMENSIONS)}")
    return PREDICATES[name](team_profile, dimension)
