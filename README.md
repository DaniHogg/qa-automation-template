# QA Automation Template (Pytest)

[![QA Template CI](https://github.com/DaniHogg/qa-automation-template/actions/workflows/ci.yml/badge.svg)](https://github.com/DaniHogg/qa-automation-template/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![pytest](https://img.shields.io/badge/pytest-8.x-green)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A)

A reusable QA automation framework for **web**, **API**, **mobile**, and optional **Windows desktop** testing.

This repository is intended to serve two purposes:

- a working portfolio project that demonstrates QA engineering patterns
- a pull-from template/library you can adapt quickly for a new team, product, or environment

The code under `src/` is the reusable layer. The tests under `tests/` are reference implementations you can keep, replace, or extend for a new project.

## Features

- **Page Object Model** – clean separation of locators and test logic  
- **API client** – reusable `HttpClient` supporting GET / POST / PUT / PATCH / DELETE  
- **Shared pytest fixtures** – reusable API client, browser session, and credential fixtures  
- **Pytest markers** – `smoke` and `regression` suites run independently  
- **Environment-driven config** – zero hard-coded URLs; override via env vars  
- **Framework unit tests** – validate reusable utilities without needing a target site  
- **Allure reporting** – rich HTML reports with step-level detail  
- **Parallel execution** – `pytest-xdist` for faster CI runs  
- **GitHub Actions CI** – runs selected suites and uploads Allure results as artefacts  

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 + pytest | Test runner and framework |
| Selenium 4 | Browser automation (Chrome / Firefox) |
| requests | HTTP API client |
| allure-pytest | Test reporting |
| pytest-xdist | Parallel test execution |
| GitHub Actions | CI/CD pipeline |
| WinAppDriver + Appium | Optional Windows desktop automation |

## Project Structure

```text
qa-automation-template/
  src/
    core/           # Settings, WebDriver factory, schema helpers, hooks
    pages/          # Page Objects and Windows desktop page objects
    clients/        # HttpClient (REST wrapper), WinAppClient
    mobile/         # Mobile placeholders
  tests/
    unit/           # Framework-level tests — no external dependency needed
    reference/
      api/          # REST API reference tests
      web/          # Selenium UI reference tests
      mobile/       # Mobile placeholder
      winapp/       # Windows desktop tests (WinAppDriver)

## How To Use This Repo In A New Role

1. Replace the target-specific environment variables.
  Set `BASE_URL`, `API_BASE_URL`, `LOGIN_USERNAME`, and `LOGIN_PASSWORD` for the new application.

2. Treat the existing tests as examples, not permanent product tests.
  The current API and web tests point at public demo services. They are useful as patterns for naming, markers, fixture usage, and page-object design.

3. Keep `src/` stable and swap `tests/` per product.
  Reuse the shared clients, config, fixtures, and page-object base classes. Add new page objects, API clients, and domain-specific fixtures for the system under test.

4. Build your suites by risk.
  Keep `smoke` for deploy-blocking checks, `regression` for broader coverage, and `unit` for framework utilities that should always run in CI.

5. Keep credentials and environment details out of test code.
  Use environment variables or CI secrets instead of hard-coded values.

## Quick Start

```bash
# Create and activate a virtual environment
python -m venv .venv && source .venv/bin/activate

# Install the project
pip install -e .

# Install optional Windows desktop dependencies
pip install -e ".[windows]"

# Run framework-level tests only
pytest -m unit

# Run only API smoke tests in parallel
pytest -m "api and smoke" -n auto

# Run only web regression tests (headless Chrome)
pytest -m "web and regression"

# Run Windows desktop tests on Windows with WinAppDriver running
pytest -m winapp

# Generate Allure report (requires Allure CLI)
allure serve allure-results
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `BASE_URL` | `https://the-internet.herokuapp.com` | Web target URL |
| `API_BASE_URL` | `https://jsonplaceholder.typicode.com` | API target URL |
| `BROWSER` | `chrome` | `chrome` or `firefox` |
| `HEADLESS` | `true` | Run browser headlessly |
| `LOGIN_USERNAME` | `tomsmith` | Demo login username |
| `LOGIN_PASSWORD` | `SuperSecretPassword!` | Demo login password |

## Current Reference Coverage

### API (`jsonplaceholder.typicode.com`)
- **Smoke** – posts, users, and todos basic availability checks
- **Regression** – CRUD lifecycle, filters, nested resources, header validation, simple response-time assertions

### Web (`the-internet.herokuapp.com`)
- **Smoke** – home page load and basic navigation assertions
- **Regression** – login flows, secure-area access, logout, checkboxes, dropdowns, dynamic loading

### Windows Desktop
- **Optional** – Notepad smoke/regression examples via WinAppDriver

### Framework Unit Tests
- configuration parsing
- HTTP client URL building

## High-Value Tests To Add For A Real Product

### API
- Authentication and authorization checks for each role
- Negative tests for invalid payloads, missing fields, and malformed requests
- Pagination, sorting, filtering, and boundary-value coverage
- Idempotency and duplicate-submission protection
- Contract validation against an OpenAPI or schema definition
- Retry, timeout, and graceful degradation behaviour

### Web
- Role-based navigation and permission boundaries
- Form validation with field-level error coverage
- File upload/download workflows
- Search, filtering, and table/grid state persistence
- Accessibility checks for critical user journeys
- Browser compatibility for the highest-risk flows
- Screenshot/video capture on failure for CI diagnostics

### Mobile
- Install/launch and first-run permission flows
- Deep links and push-notification entry points
- Offline/poor-network behaviour
- Session persistence, biometric login, and logout paths

### Windows Desktop
- Launch and attach-to-existing-session coverage
- Save/Open/Export workflows and file dialog handling
- Keyboard shortcut behaviour
- Error dialogs, unsaved-change prompts, and recovery paths
- Data import/export validation

## Notes For Using This As A Library

- Prefer adding generic helpers to `src/` and product-specific assertions to `tests/`.
- Keep demo endpoints and demo credentials isolated behind config.
- Add unit tests whenever you add reusable helpers, wrappers, parsers, or fixtures.
- In CI, run `unit` tests on every change and only run environment-dependent suites when the target environment is available.
- If a team has multiple services or apps, split tests by domain and keep shared fixtures in `tests/conftest.py` or dedicated helper modules.

## Practical Next Improvements

- Add screenshot-on-failure and request/response logging hooks.
- Add schema validation helpers for API responses.
- Add test-data factories or builders for complex entities.
- Add separate CI jobs for `unit`, `api`, `web`, and optional `winapp` suites.
