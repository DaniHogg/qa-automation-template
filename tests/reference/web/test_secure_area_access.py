import pytest

from pages.example_page import LoginPage
from pages.secure_area_page import SecureAreaPage


@pytest.mark.web
@pytest.mark.regression
def test_secure_area_accessible_after_login(driver, valid_login_credentials):
    login = LoginPage(driver)
    login.open()
    login.login(valid_login_credentials["username"], valid_login_credentials["password"])

    secure = SecureAreaPage(driver)
    assert secure.is_on_secure_area()
    assert "Secure Area" in secure.heading_text()
