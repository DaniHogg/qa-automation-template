import pytest

from pages.portfolio_page import PortfolioHomePage


@pytest.mark.web
@pytest.mark.smoke
def test_home_page_has_heading(driver):
    page = PortfolioHomePage(driver)
    page.open()
    assert "Live Automation Results" in page.heading_text()
