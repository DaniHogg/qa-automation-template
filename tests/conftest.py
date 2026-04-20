import pytest

from core.driver_factory import build_web_driver


@pytest.fixture(scope="session")
def api_headers():
    return {"Accept": "application/json"}


@pytest.fixture(scope="function")
def driver():
    browser = build_web_driver()
    yield browser
    browser.quit()
