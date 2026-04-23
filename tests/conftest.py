import logging

import allure
import pytest
from allure_commons.types import AttachmentType

from clients.http_client import HttpClient
from core.config import settings
from core.driver_factory import build_web_driver
from core.hooks import attach_logging_adapter, _take_screenshot

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(name)s: %(message)s")


@pytest.fixture(scope="session")
def api_headers():
    return {"Accept": "application/json"}


@pytest.fixture(scope="session")
def api_client():
    client = HttpClient()
    attach_logging_adapter(client.session)
    return client


@pytest.fixture(scope="session")
def valid_login_credentials():
    return {
        "username": settings.login_username,
        "password": settings.login_password,
    }


@pytest.fixture(scope="session")
def invalid_login_credentials():
    return {
        "username": "invalid-user",
        "password": "invalid-password",
    }


@pytest.fixture(scope="function")
def driver(request):
    browser = build_web_driver()
    yield browser
    # rep_call is absent when setup fails or test is skipped before call phase.
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call is not None and rep_call.failed:
        path = _take_screenshot(browser, request.node.nodeid)
        if path:
            allure.attach.file(
                str(path),
                name="failure-screenshot",
                attachment_type=AttachmentType.PNG,
            )
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
