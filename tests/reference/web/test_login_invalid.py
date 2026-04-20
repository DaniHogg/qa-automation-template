import pytest

from pages.example_page import LoginPage


@pytest.mark.web
@pytest.mark.regression
def test_invalid_login_shows_error_message(driver, invalid_login_credentials):
    page = LoginPage(driver)
    page.open()
    page.login(invalid_login_credentials["username"], invalid_login_credentials["password"])
    flash = page.flash_text()
    assert "Your username is invalid!" in flash
