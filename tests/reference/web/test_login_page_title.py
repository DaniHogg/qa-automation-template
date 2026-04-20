import pytest

from pages.example_page import LoginPage


@pytest.mark.web
@pytest.mark.regression
def test_login_page_title(driver):
    page = LoginPage(driver)
    page.open()
    assert "Login Page" in driver.title or "Form Authentication" in driver.page_source
