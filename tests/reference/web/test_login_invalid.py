import pytest

from pages.portfolio_page import PortfolioHomePage


@pytest.mark.web
@pytest.mark.regression
def test_home_lede_explains_dashboard_scope(driver):
    page = PortfolioHomePage(driver)
    page.open()
    assert "Status, freshness" in page.lede_text()
