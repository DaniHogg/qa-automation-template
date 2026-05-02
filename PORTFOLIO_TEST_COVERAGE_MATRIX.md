# qa-automation-template Coverage Matrix for Portfolio Site

This matrix maps discovered tests to required portfolio-site functions.

## Discovered Test Suites
- api: 3 test files
- unit: 4 test files
- reference/api: 15 test files
- reference/web: 12 test files
- reference/winapp: 4 test files

Source note:
- Default pytest runs target tests path and exclude reference by default through pytest config behavior.
- Reference suites should be represented as optional or on-demand coverage, not implied as always executed.

## Required Portfolio Functions by Suite

## api (default)
- Show latest status and totals for API suite from normal CI runs when available.
- Link to API evidence (Allure, JUnit, or workflow logs).
- Show suite notes for endpoint scope (posts, users, todos).

## unit (default)
- Show framework health status as a separate suite.
- Keep this suite highly visible to demonstrate maintainability checks.

## reference/api (optional library)
- Display as reference coverage or expanded regression library.
- Show execution status only when explicitly run; otherwise mark as not-run with reason.

## reference/web (optional library)
- Display as UI reference scenarios.
- Preserve skipped/not-run states for runs where browser suites were not executed.

## reference/winapp (platform-gated)
- Label as Windows-only desktop automation.
- Require explicit prerequisite annotation (WinAppDriver + Windows agent).
- Never mark absent execution as failure when platform is unavailable.

## Cross-Suite Site Behavior Requirements
- Status taxonomy: passed, failed, skipped, not-run, stale.
- Freshness policy: stale after 7 days.
- History policy: rolling latest 5 runs only.
- Truth policy: always show why a suite did not run.
- Evidence policy: one-click links to workflow runs and report artifacts.

## UI/Information Architecture Requirements
- Project card:
  - latest overall status
  - last completed time
  - stale badge
  - quick evidence links
- Project detail:
  - suite table with status and totals
  - latest 5 runs timeline
  - prerequisite notes per suite
- Report drill-down:
  - suite-level artifact links
  - trigger context (push, pull request, manual dispatch)

## Minimum Data Fields Needed
- run id, commit sha, branch, workflow run url
- started/completed timestamps and duration
- status totals (pass/fail/skip/error)
- suite-level notes and prerequisite flags
- stale threshold metadata (7 days)
- history limit metadata (5)
