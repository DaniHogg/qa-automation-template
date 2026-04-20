import pytest

from pages.example_page import LoginPage


@pytest.mark.web
@pytest.mark.regression
def test_invalid_login_shows_error_message(driver):
    page = LoginPage(driver)
    page.open()
    page.login("wronguser", "wrongpass")
    flash = page.flash_text()
    assert "Your username is invalid!" in flash
