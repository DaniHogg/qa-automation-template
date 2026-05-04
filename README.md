
# QA Automation Template (Pytest)

A **production-style QA automation framework** designed to demonstrate how I approach test automation in a real engineering environment.

This repository is intentionally structured to reflect how automated testing is implemented and maintained within a product team — covering **UI automation, API testing, configuration management, CI/CD, and test scalability**.

> This is my **flagship automation project**.  
> Other repositories in my GitHub profile demonstrate individual tools or concepts; this repo shows how they come together in practice.

---

## 🎯 Purpose of This Repository

This project exists to demonstrate:
- How I design **maintainable automation frameworks**
- How UI, API, and test infrastructure fit together
- How automated tests are executed in CI, not just locally
- How I balance simplicity with scalability in test design

It is **not** a tutorial repo and it is **not** over‑engineered for demonstration purposes.

---

## 🧱 Key Design Principles

- **Clear separation of concerns**
  - Test logic ≠ locators ≠ infrastructure
- **Environment-driven configuration**
  - No hard-coded URLs or credentials
- **Explicit test intent**
  - Smoke vs regression suites are clearly defined
- **CI-first mindset**
  - Tests are designed to run headlessly and reliably in pipelines

---

## 🛠 Tech Stack

| Tool | Purpose |
|-----|--------|
| Python 3.11 | Core language |
| pytest | Test runner and framework |
| Selenium 4 | Browser automation |
| requests | API client |
| allure-pytest | Rich test reporting |
| pytest-xdist | Parallel execution |
| GitHub Actions | CI pipeline |

---

## 📁 Project Structure
qa-automation-template/
├── src/
│   ├── core/        # Settings, WebDriver factory, shared utilities
│   ├── pages/       # Page Objects (BasePage, HomePage, LoginPage)
│   ├── clients/     # Reusable API client (REST wrapper)
│   └── mobile/      # Mobile placeholders (future extension)
│
├── tests/
│   ├── web/         # Selenium UI tests
│   ├── api/         # REST API tests
│   └── mobile/
│
├── .github/workflows/
│   └── ci.yml       # GitHub Actions pipeline
│
├── pytest.ini       # Markers (smoke, regression, api, web)
└── pyproject.toml

This structure mirrors what I’ve seen work effectively in real QA teams.

---

## ✅ Test Coverage

### API Tests
Target API: `jsonplaceholder.typicode.com`

- Smoke
  - Basic availability and response validation
- Regression
  - Full CRUD lifecycle
  - Data validation
  - Nested resources (e.g. comments)
  - Filtering and query parameters

### Web UI Tests
Target site: `danihogg.github.io/qa-portfolio-livesite`

- Smoke and regression checks validate portfolio dashboard and project-detail pages.
- Structured using Page Object Model.
- One coverage-link assertion test is skip-gated when the target deployment does not yet include the coverage panel.
- Designed to run headless in CI.

## ⚙️ Configuration & Environment Variables

| Variable | Default | Description |
|--------|--------|-------------|
| BASE_URL | https://danihogg.github.io/qa-portfolio-livesite/ | Web target |
| WEB_TARGET_PROFILE | qa_portfolio_live_site | Contract profile for web routes/selectors/keyword expectations |
| WEB_DASHBOARD_PATH | dashboard.html | Dashboard route appended to BASE_URL when BASE_URL is site root |
| WEB_PROJECT_CARDS_SELECTOR | #project-cards | CSS selector for the dashboard project-cards container |
| WEB_HEADING_KEYWORDS | automation,results,evidence | Comma-separated keywords accepted for dashboard heading checks |
| WEB_TITLE_KEYWORDS | automation,results,evidence | Comma-separated keywords accepted for page-title checks |
| WEB_LEDE_KEYWORDS | ci,status,workflow | Comma-separated keywords accepted for dashboard lede checks |
| API_BASE_URL | https://jsonplaceholder.typicode.com | API target |
| API_TARGET_PROFILE | jsonplaceholder | Contract profile for API endpoints/expectations |
| API_REQUEST_TIMEOUT | 15 | Request timeout in seconds for all API calls |
| API_SUCCESS_STATUS | 200 | Expected HTTP status code for successful API requests |
| API_CREATED_STATUS | 201 | Expected HTTP status code for resource creation (POST) |
| API_ACCEPTED_STATUS | 200 | Expected HTTP status code for accepted async operations |
| API_NOT_FOUND_STATUS | 404 | Expected HTTP status code for not-found responses |
| API_RESPONSE_TIME_THRESHOLD | 3.0 | Maximum allowed response time in seconds for performance checks |
| API_MIN_LIST_ITEMS | 1 | Minimum number of items expected in list-response assertions |
| API_CONTENT_TYPE | application/json | Expected Content-Type header in API responses |
| BROWSER | chrome | chrome or firefox |
| HEADLESS | true | CI-friendly execution |

**Web tests** check heading/title/lede with intent-based keyword matching (configurable via comma-separated env vars), not exact copy.
**API tests** are profile-driven: timeouts, status codes, and performance thresholds come from the contract, making it easy to adapt to different targets or service-level expectations.

### CI Lanes
- `quick-linux` (push/pull request): unit + API smoke + web smoke against portfolio site.
- `full-linux` (workflow_dispatch/schedule): unit + API smoke/regression + web smoke/regression against portfolio site.
- `winapp-windows` (workflow_dispatch/schedule): Windows desktop reference tests with WinAppDriver.
- `merge-allure`: merges all available lane artifacts into `allure-results` for downstream portfolio ingestion.

## 🚀 Running the Tests

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install the project
pip install -e .

# Run full test suite
pytest

# Run API smoke tests in parallel
pytest -m "api and smoke" -n auto

# Run web regression tests
pytest -m "web and regression"
```

## 📊 Reporting

Allure reports generated during execution
CI uploads test artefacts for visibility
Designed for fast triage, not just “pretty output”

## 🧭 What This Repo Intentionally Does NOT Do

Hard-code waits or sleeps
Hide complexity in magic helpers
Use brittle locators without justification
Assume a single environment or execution mode

## ✅ How to Review This Repo
If you’re reviewing this repository:

Start with src/core to see how drivers and config are handled
Look at clients/HttpClient for API abstraction
Review Web vs API test separation
Check .github/workflows/ci.yml for execution strategy

## 📌 Related Repositories

Postman-API-Tests – API testing using Postman collections
Selenium – Focused Selenium + pytest examples
Beginners-Playwright – Modern Playwright automation basics
