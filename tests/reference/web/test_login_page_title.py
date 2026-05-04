import pytest

from pages.portfolio_page import PortfolioHomePage


@pytest.mark.web
@pytest.mark.regression
def test_login_page_title(driver):
    page = PortfolioHomePage(driver)
    page.open()
    assert "Live Automation Results" in driver.title
