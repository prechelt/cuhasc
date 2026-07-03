title: Handbook: add one-low trigger support
state: open
labels: ready-for-agent
---

# Handbook: add one-low trigger support

## Parent

#1

## What to build

Extend the Trigger grammar and evaluator in `cuhasc/handbook.py` (built in #2) to support
`one-low(DIM)`, symmetric to the existing `one-high(DIM)`: it fires when at least one
Member in `team_profile['members']` has a Score on `DIM` that is Low (Score ≤ 2).

Add one more example Handbook Section file under `handbook/` using `one-low(DIM)` for
some Dimension, so the full set of example Sections includes both Trigger kinds.

No changes to the `show_team` wiring or template should be needed — `one-low` Sections
flow through the same "get triggered Sections, render below the plot, Dimension order,
no attribution" path already built in #2.

## Acceptance criteria

- [ ] `cuhasc/handbook.py` recognizes `one-low(DIM)` triggers
- [ ] A Member Score of exactly 2 triggers `one-low`; a Score of exactly 3 does not
- [ ] `handbook/` has an example Section using `one-low(DIM)`
- [ ] A Team with one Member triggering a `one-high` Section and another (different Dimension) triggering a `one-low` Section shows both Sections on `show_team`, in Dimension order (`PO, UN, CO, LT, MA`), regardless of which Trigger kind fired
- [ ] `cuhasc/test/test_handbook.py` covers `one-low` parsing/evaluation including the Score-2 boundary
- [ ] `cuhasc/test/test_views.py` covers the mixed `one-high` + `one-low` simultaneous-triggering scenario above

## Blocked by

- #2 (Handbook mechanism MVP: one-high trigger renders on show_team)
