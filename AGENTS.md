
This is a Django project following all the usual Django conventions.
Testing uses pytest, pytest-django, pytest-cov (already installed).
Find a project overview in README.md.

Project-specific conventions:
- Declare parameter and result types for functions, except duck-typed params or `None` results. 
  Declare class attributes. Do not declare local variables.
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

## Agent skills

- Issues and PRDs are tracked as GitHub issues (via the `gh` CLI). 
  See `docs/agents/issue-tracker.md`.
- We use canonical issue labels for issue states (triage roles).
  See `docs/agents/triage-labels.md`.
- We use a single design space, not several: one `CONTEXT.md` + `docs/adr/` at the repo root.
  See `docs/agents/domain.md`.
