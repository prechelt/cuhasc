
This is a Django project following all the usual Django conventions.
Testing uses pytest, pytest-django, pytest-cov (already installed).
Find a project overview in README.md.

## Commands

- Install deps: `uv sync`.
- Run the dev server: `python manage.py runserver` (uses `CUHASC_DEBUG=1` and a well-known
  dev secret key automatically; DB is `db.sqlite3` in the checkout root; migrations are not
  a separate step during development, but `manage.py runserver` doesn't auto-apply them --
  run `python manage.py migrate` after adding one).
- Run the installed CLI instead, if you need to exercise deployment-mode behavior
  (data dir resolution, waitress, banner/URLs, backup/restore): `python -m cuhasc.cli run|info|adminpage|backup|restore|manage ...`,
  or after `pip install -e .`, plain `cuhasc ...`.
- Run all tests: `pytest`.
- Run one test file: `pytest cuhasc/test/test_views.py`.
- Run one test: `pytest cuhasc/test/test_views.py::test_show_member_requires_correct_token` (or `-k <substr>`).
- Coverage: `pytest --cov=cuhasc --cov-report=term-missing`.
- Django system checks: `python manage.py check` (and `--deploy`, whose four TLS warnings
  are expected -- see docs/adr/0003).
- Make a release: see docs/RELEASING.md.

Project-specific conventions:
- Declare parameter and result types for functions, except duck-typed params or `None` results. 
  Declare class attributes. Do not declare local variables.
- Position private helper functions at the end of their file, in alphabetical order.
- Tests for module `abc.defg` go into module `abc.test.test_defg`.
- Use special pytest mechanisms (e.g. parametrize) where truly useful.
- Adding a test means adding an assertion, not necessarily a new test function:
  When tests can share the same scenario, prefer collecting all assertions (and possibly additional
  scenario steps in between) in one function for the happy path cases and another for
  the test cases.
- Tests focussing on interface function `myfunction()` are called `test_myfunction_has_expected_behavior`
  for complex cases. Several simple cases should go together in `test_myfunction_ok` (happy path) or
  `test_myfunction_error` (error cases).
- Tests focussing on the interplay of several interface functions get an appropriate ad-hoc name.

Behavior conventions:
- If the session is interactive and any substantial design aspect is ambiguous, discuss it with me.

## Architecture

CuHaSc has no accounts: a Team or Member is identified by an unguessable token in the URL
(`cuhasc/base.py::random_token`), backed up by a cookie (`cuhasc/cookies.py::CuhascCookie`)
that remembers which Teams/Members this browser has touched so `home` can list them again.
`models.py` (`Team`, `Member`, `QResult`, plus the `AdminPage` singleton for cookie recovery)
is the only persisted state; everything else is computed or loaded from files at import time.

Two content stores are eager-loaded from disk into module-level globals when their module is
first imported, then served purely from memory (never touched again per-request):
- `instruments.py` loads the questionnaire, its answer scales, and Dimension names from
  `cuhasc/data/instruments/{cvscale,scales,dimensions}-<lang>.csv|tsv`, one language per file
  triplet; `get_languages()` is the intersection of the three sets actually present.
- `handbook.py` loads Handbook Sections (Markdown + YAML frontmatter, see CONTEXT.md) from
  `cuhasc/data/handbook/<chapter>-<slug>.md`. Each Section's `trigger` is one Predicate call
  (`one-high(PO)` etc.) evaluated by `evaluate()` against a Team Culture Profile; the fixed
  Predicate table lives in `handbook.PREDICATES`.

Request flow (`views.py`): a view resolves Team/Member by id+token
(`get_object_or_404`), reads/writes the cookie for the "known Teams/Members" list and the
language preference, and for the questionnaire language decides between the cookie, the
`Accept-Language` header, and English (see ADR-0002 for why language switching is a POST that
preserves in-progress answers rather than a GET/refresh). `Team.culture_profile()` /
`Member.culture_profile()` on the models aggregate `QResult` rows into Scores; `plots.py`
renders those as inline SVG (ADR-0001 explains why not matplotlib/JS).

`cli.py` is the entire UI of an installed deployment (the `cuhasc` command: `run`, `info`,
`adminpage`, `backup`, `restore`, `manage`) and is what a non-developer Culture Lead actually
uses; `deployment.py` resolves the checkout-vs-installed split (data dir, secret key, allowed
hosts, public URL) that `settings.py` reads from. `cli.main()` must set environment variables
and create the data directory *before* `django.setup()` -- see the module docstrings of both
files before changing deployment behavior. Read ADR-0003 before touching `ALLOWED_HOSTS`,
the secret-key fallback, or the tunnel/`SECURE_PROXY_SSL_HEADER` handling; all three look like
bugs out of context but are deliberate.

## Agent skills

- Issues and PRDs are tracked as GitHub issues (via the `gh` CLI). 
  See `docs/agents/issue-tracker.md`.
- We use canonical issue labels for issue states (triage roles).
  See `docs/agents/triage-labels.md`.
- We use a single design space, not several: one `CONTEXT.md` + `docs/adr/` at the repo root.
  See `docs/agents/domain.md`.
