title: Handbook mechanism MVP: one-high trigger renders on show_team
state: open
labels: ready-for-agent
---

# Handbook mechanism MVP: one-high trigger renders on show_team

## Parent

#1

## What to build

Build the end-to-end Handbook mechanism for a single Trigger kind, `one-high(DIM)`, and
show its result on the `show_team` page.

A new top-level `handbook/` directory holds Handbook Section files: one Markdown file
per Section, each with YAML topmatter (`title`, `trigger`) followed by a Markdown body
(the advice text) — the same "topmatter + body" shape already used by the Markdown-file
issue tracker. Add two example Section files for this ticket, each triggering on a
different Dimension (e.g. one `one-high(PO)`, one `one-high(UN)`), so ordering can be
demonstrated.

Add a new `cuhasc/handbook.py` module, structured like `cuhasc/instruments.py`: it loads
all `handbook/*.md` files at import time via a glob, parsing topmatter with `PyYAML` and
the Markdown body with the `markdown` library (add both as new `pyproject.toml`
dependencies). It exposes a function that, given a Team Culture Profile dict (the shape
returned by `Team.culture_profile()`), returns the list of Handbook Sections whose
Trigger is fulfilled, ordered by Dimension order `PO, UN, CO, LT, MA` (matching
`views.DIMENSION_ORDER`).

`one-high(DIM)` fires when at least one Member in `team_profile['members']` has a Score
on `DIM` that is High (Score ≥ 4).

Wire this into `views.show_team`: compute the triggered Section list and pass rendered
HTML for each into the template context. `show_team.html` renders the triggered Sections
below the existing plot SVG, generically — no mention of which Member triggered which
Section (consistent with the existing member-label-hidden-by-default privacy pattern).
When zero Sections trigger, render nothing extra (no empty placeholder block). Markdown
output is inserted via Django's `mark_safe`, consistent with how the existing SVG
functions are marked safe — safe here because Section files are trusted, developer
authored repository content, never user-submitted (see ADR-0003).

## Acceptance criteria

- [ ] `pyproject.toml` lists `markdown` and `PyYAML` as dependencies
- [ ] `handbook/` directory exists with at least two example Section files (YAML topmatter `title`+`trigger` + Markdown body), each with a different Dimension in its `one-high` trigger
- [ ] `cuhasc/handbook.py` loads and parses all `handbook/*.md` files at import time
- [ ] Given a Team Culture Profile dict, `handbook.py` returns the correct list of triggered Sections for `one-high(DIM)`, ordered by Dimension order `PO, UN, CO, LT, MA`
- [ ] Boundary behavior is correct: a Member Score of exactly 4 triggers `one-high`; a Score of exactly 3 does not
- [ ] `show_team` renders a triggered Section's title and body content below the plot
- [ ] `show_team` does not render a Section whose Trigger is not fulfilled
- [ ] `show_team` for a Team with no Members with answers (no Culture Profile) renders no Handbook content
- [ ] When two Sections trigger simultaneously (different Dimensions), both appear, in Dimension order
- [ ] No Member name or identifying detail appears near a triggered Section
- [ ] `cuhasc/test/test_handbook.py` exists, covering the parsing and trigger-evaluation acceptance criteria above using fixture/monkeypatched Section data (not the real `handbook/` content)
- [ ] `cuhasc/test/test_views.py` is extended to cover the `show_team` rendering acceptance criteria above, following the existing `team_with_answers` fixture pattern

## Blocked by

None - can start immediately
