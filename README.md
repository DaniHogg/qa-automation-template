# QA Automation Template (Pytest)

[![QA Template CI](https://github.com/DaniHogg/qa-automation-template/actions/workflows/ci.yml/badge.svg)](https://github.com/DaniHogg/qa-automation-template/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![pytest](https://img.shields.io/badge/pytest-8.x-green)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A)

A production-ready automation framework template for **web**, **API**, and **mobile** testing.  
Designed to demonstrate QA engineering best practices: Page Object Model, fixture-based configuration, CI/CD integration, and structured test organisation.

## Features

- **Page Object Model** – clean separation of locators and test logic  
- **API client** – reusable `HttpClient` supporting GET / POST / PUT / PATCH / DELETE  
- **Pytest markers** – `smoke` and `regression` suites run independently  
- **Environment-driven config** – zero hard-coded URLs; override via env vars  
- **Allure reporting** – rich HTML reports with step-level detail  
- **Parallel execution** – `pytest-xdist` for faster CI runs  
- **GitHub Actions CI** – runs API and web suites with Chrome, uploads Allure results as artefacts  

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 + pytest | Test runner and framework |
| Selenium 4 | Browser automation (Chrome / Firefox) |
| requests | HTTP API client |
| allure-pytest | Test reporting |
| pytest-xdist | Parallel test execution |
| GitHub Actions | CI/CD pipeline |

## Project Structure

```text
qa-automation-template/
  src/
    core/           # Settings, WebDriver factory
    pages/          # Page Objects (BasePage, HomePage, LoginPage)
    clients/        # HttpClient (REST wrapper)
    mobile/         # Mobile placeholders
  tests/
    web/            # Selenium UI tests (smoke + regression)
    api/            # REST API tests (smoke + regression)
    mobile/
  config/
  .github/workflows/ci.yml
```

## Quick Start

```bash
# Create and activate a virtual environment
python -m venv .venv && source .venv/bin/activate

# Install the project
pip install -e .

# Run the full test suite
pytest

# Run only API smoke tests in parallel
pytest -m "api and smoke" -n auto

# Run only web regression tests (headless Chrome)
pytest -m "web and regression"

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

## Test Coverage

### API (`jsonplaceholder.typicode.com`)
- **Smoke** – GET /posts returns 200, schema validation
- **Regression** – full CRUD lifecycle (POST / PUT / PATCH / DELETE), filter by userId, nested resources (comments)

### Web (`the-internet.herokuapp.com`)
- **Smoke** – home page loads, example links present
- **Regression** – valid and invalid form authentication, page content assertions

## Portfolio Notes

- Extend with additional page objects for `DynamicLoading`, `Checkboxes`, `Dropdown`, etc.
- Add `conftest.py` fixtures for test data factories.
- Add screenshot-on-failure using `pytest` hooks for richer failure artefacts.
