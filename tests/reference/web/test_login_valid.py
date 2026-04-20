import pytest

from pages.example_page import LoginPage


@pytest.mark.web
@pytest.mark.regression
def test_valid_login_shows_success_message(driver, valid_login_credentials):
    page = LoginPage(driver)
    page.open()
    page.login(valid_login_credentials["username"], valid_login_credentials["password"])
    flash = page.flash_text()
    assert "You logged into a secure area!" in flash
