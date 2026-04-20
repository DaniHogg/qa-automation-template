import pytest

from pages.example_page import LoginPage


@pytest.mark.web
@pytest.mark.regression
def test_valid_login_shows_success_message(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    flash = page.flash_text()
    assert "You logged into a secure area!" in flash
