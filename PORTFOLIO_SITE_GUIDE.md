# Portfolio Site Guide for qa-automation-template

This guide defines hosting options and required site functionality to represent this project truthfully to potential employers.

## Recommended Hosting (Static-First)

## Primary Recommendation
- GitHub Pages with GitHub Actions deployment.
- Why:
  - Tight integration with repository workflows.
  - Simple static deployment and low maintenance.
  - Easy provenance links back to workflow runs and commits.

## Good Alternatives
- Netlify:
  - Great preview deploys and simple static hosting.
- Cloudflare Pages:
  - Fast global CDN and low-cost static delivery.

## Use Server-Backed Only If Needed
Use a backend only when you need private artifact proxying, authenticated APIs, or near-real-time filtering not feasible at build time.

## Required Site Functions

## 1) Project Summary Card
Each card must show:
- Project name and purpose.
- Framework stack (pytest, selenium, requests, allure).
- Latest overall run status (passed/failed/skipped/partial).
- Latest completion timestamp.
- Stale badge when older than 7 days.
- Quick links to workflow run and report artifacts.

## 2) Suite-Level Visibility for qa-automation-template
Your site must model these suites separately:
- unit
- api-smoke
- api-regression
- web-smoke
- web-regression

Why this matters:
- In this repository, API and web suites are gated by workflow_dispatch in CI.
- If not executed in a run, they should appear as skipped with explicit reason, not omitted.

## 3) History Window
- Keep and display only latest 5 runs.
- Provide trend chips or a compact table showing status and time for each run.

## 4) Truthful Skip/Prerequisite Reporting
For each skipped suite, show a reason:
- trigger-gated (for example workflow_dispatch only)
- environment missing
- credentials missing
- platform-specific requirement missing

## 5) Evidence Links
For each run/suite, support links to:
- workflow run URL
- Allure results artifact or report
- screenshots artifact when present

## 6) Data Freshness System
- Evaluate staleness as now - latest.completed_at > 7 days.
- Show last refreshed timestamp for site data ingestion.

## 7) Build-Time Link Validation
- Fail build if required links are malformed.
- Warn (not fail) if optional screenshot artifacts are absent.

## 8) Failure-Safe Ingestion
- If one project's extraction fails, keep previous known-good data for that project and continue publishing others.

## Data Model Expectations
Use normalized JSON per project:
- data/projects/qa-automation-template/latest.json
- data/projects/qa-automation-template/runs/<run-id>.json

Required fields:
- run id, status, timestamps, duration
- pass/fail/skip/error totals
- suite-level breakdown
- source run metadata (workflow, branch, commit, run URL)
- stale threshold (7 days)
- history cap (5)

## MVP Implementation Order
1. Build extractor for qa-automation-template workflow + Allure artifacts.
2. Publish normalized latest + history JSON.
3. Build one static card + detail page consuming JSON.
4. Add stale badge and 5-run retention checks.
5. Add link validator in site build pipeline.
6. Expand to Playwright, Selenium, Appium, API-testing-pytest, Postman, k6.
