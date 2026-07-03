title: Handbook Sections: show triggered advice on show_team
state: open
labels: ready-as-parent
---

# Handbook Sections: show triggered advice on show_team

## Problem Statement

A Culture Lead who has gathered a Team's Team Culture Profile only sees five numbers
plotted on a [1,5] scale. The plot tells them *what* their Team's culture profile looks
like, but not *what it means* or *what to do about it*. Without domain expertise in the
Hofstede dimensions, a Culture Lead has no way to translate a profile like "low
Collectivism, high Power Distance" into concrete guidance for how that might show up in
the Team's day-to-day work, or what to watch out for.

## Solution

Introduce a Handbook: a curated set of short advice pieces, each a **Handbook Section**.
Each Section declares a **Trigger** (e.g. "at least one Team Member scored High on Power
Distance") and a Markdown body with the actual advice. When a Team's Team Culture
Profile fulfills a Section's Trigger, Cuhasc shows that Section, rendered from Markdown,
below the plot on the `show_team` page. Advice is shown generically, without revealing
which Member's Score caused it to appear.

## User Stories

1. As a Culture Lead, I want to see relevant advice below my Team's Culture Profile plot, so that I can act on the assessment instead of just looking at a plot.
2. As a Culture Lead, I want the advice to reference concrete Dimensions (Power Distance, Uncertainty Avoidance, Collectivism, Long-Term Orientation, Masculinity), so that I understand which aspect of team culture it addresses.
3. As a Team Member, I want the shown advice to never reveal whose Score triggered it, so that individual answers stay private within the Team.
4. As the developer/researcher maintaining Cuhasc, I want to author Handbook Sections as plain Markdown files with YAML topmatter, so that I can add or edit advice without touching Python code or the database.
5. As a developer, I want a Handbook Section to declare a Trigger such as `one-high(PO)`, so that advice is only shown when it's actually relevant to the Team's profile.
6. As a developer, I want Trigger conditions to reference the same Dimension codes (`PO`, `UN`, `CO`, `LT`, `MA`) used by the questionnaire and the plots, so there's one consistent vocabulary across the app.
7. As a Culture Lead, I want all currently-relevant Handbook Sections to be shown together, so I don't miss advice because only one item is displayed.
8. As a Culture Lead, I want the shown Sections to appear in a stable, predictable order (grouped by Dimension, in the same PO/UN/CO/LT/MA order as the plot), so the advice reads coherently alongside the plot.
9. As a Culture Lead, I want no Handbook Sections to show up for a Team with no Culture Profile yet (no Members with answers), so the page doesn't show broken or misleading advice.
10. As a Culture Lead, I want a Team with zero triggered Sections to still look intentional (no empty placeholder block), so the page doesn't look broken.
11. As a developer, I want Handbook Section bodies to support Markdown formatting (headings, lists, links, images), so advice can be written with proper structure and references.
12. As a developer, I want a Section's `title` and `trigger` defined via YAML topmatter, so metadata and content are separated the same way it already works for the Markdown-file issue tracker.
13. As a developer, I want Handbook Sections loaded from files at Django startup (like `instruments.py` loads questionnaire content), so no database migration or admin UI is needed to manage advice content.
14. As a developer, I want "Score is High" (≥4) and "Score is Low" (≤2) formally and consistently defined, so Trigger evaluation is unambiguous across all Sections.
15. As a maintainer, I want it to be possible to add further kinds of Trigger conditions later (beyond `one-high`/`one-low`) without redesigning the file format or loading mechanism, so the advice vocabulary can grow.
16. As a developer, I want automated tests proving a Team profile matching a Trigger causes that Section to render, and a non-matching profile does not, so regressions are caught.
17. As a Culture Lead, I want Handbook Sections to load correctly regardless of *which* Team Member's Score triggered them, so Sections triggered by different Members can co-occur on the same page.

## Implementation Decisions

- New top-level `handbook/` directory at the repo root holding Handbook Section files: one Markdown file per Section, English-only for now (no per-language split, unlike `instruments/`).
- Each file has YAML topmatter with at least `title` and `trigger` fields, followed by a Markdown body (the advice text) — the same "YAML topmatter + body" shape already used by the Markdown-file issue tracker (`docs/agents/issue-tracker.md`).
- New module `cuhasc/handbook.py`, structured like `cuhasc/instruments.py`: loads all `handbook/*.md` files at import time via a glob, parsing topmatter with `PyYAML` and the body with the `markdown` library (both to be added as new dependencies in `pyproject.toml`).
- `handbook.py` exposes a function that, given a Team Culture Profile dict (the shape returned by `Team.culture_profile()`), returns the ordered list of Handbook Sections whose Trigger is fulfilled — ordered by Dimension order `PO, UN, CO, LT, MA` (matching `views.DIMENSION_ORDER`).
- Trigger grammar for this PRD: `one-high(DIM)` and `one-low(DIM)`, where `DIM` is one of `PO, UN, CO, LT, MA`. A Trigger fires when at least one Member in `team_profile['members']` has a Score on that Dimension that is High (≥4) or Low (≤2) respectively. The loader/evaluator design should not preclude adding further Trigger kinds later.
- `views.show_team` computes the triggered list via `handbook.py` and passes the rendered HTML for each Section into the `show_team.html` template context, displayed below the existing plot SVG.
- Rendered Markdown output is inserted via Django's `mark_safe`, consistent with how `culture_profile_svg`/`team_culture_profile_svg` output is already marked safe — safe here because Handbook Section files are trusted, developer-authored repository content, never user-submitted (see ADR-0003).
- No attribution of which Member triggered a Section is rendered — Sections are shown generically, consistent with the existing member-label-hidden-by-default privacy pattern already present in the plot.
- Domain language and architecture already recorded ahead of implementation: `CONTEXT.md` gained the terms **Handbook Section**, **Trigger**, **High Score**/**Low Score**; `docs/adr/0003-handbook-sections-as-static-files.md` records the static-file-over-DB-model decision.

## Testing Decisions

- A good test here asserts observable behavior — whether a Section's rendered text appears on `show_team` for a given set of Member answers, or whether `handbook.py`'s pure functions correctly parse a file and correctly decide whether a Trigger fires for a profile — not internal call sequencing.
- `cuhasc/test/test_handbook.py` (new, mirrors `cuhasc/test/test_instruments.py`): tests topmatter/body parsing for a Section file, and tests `one-high`/`one-low` evaluation against constructed Team Culture Profile dicts, including boundary values (Score exactly 4, exactly 2, exactly 3).
- `cuhasc/test/test_views.py` (extend existing file): tests via the Django test client against `show_team`, following the existing `team_with_answers` fixture pattern — assert a Section's title/content appears when a Member's Score meets its Trigger, is absent when it doesn't, and that a Team with no Members with answers shows no Handbook content.
- Tests use fixture Handbook Section data (constructed in-memory or monkeypatched, following the `test_get_languages_requires_questionnaire_scales_and_dimensions` monkeypatch pattern in `test_instruments.py`) rather than the real `handbook/` content, so tests don't break when real advice content is edited.

## Out of Scope

- The full Trigger vocabulary beyond `one-high`/`one-low` (e.g. triggers on the team mean Score, multi-Dimension/compound triggers, thresholds other than 4/2) — explicitly deferred by the project owner to a future PRD.
- Localization of Handbook Section content (e.g. German translation) — English only for now.
- Any admin UI or DB-backed authoring workflow for Handbook Sections.
- Attribution of which Member triggered a Section.
- Displaying Handbook Sections on `show_member` (the individual profile page) — only `show_team` is in scope.
- Authoring the actual advice content for all five Dimensions × High/Low (10 sections worth of text) — this PRD covers the mechanism; content authoring can follow as separate child issues.

## Further Notes

- This PRD reflects decisions reached in a grill-with-docs session (2026-07-02/03): Dimension codes use the app's existing `PO`/`UN`/`CO`/`LT`/`MA` (not the `PD` shorthand from Hofstede literature), Triggers evaluate individual Member Scores rather than the team mean, and High/Low use a fixed 4/2 cutoff.
- See `CONTEXT.md` (Handbook Section, Trigger, High/Low Score) and `docs/adr/0003-handbook-sections-as-static-files.md` for the recorded domain language and architecture decision behind this feature.
