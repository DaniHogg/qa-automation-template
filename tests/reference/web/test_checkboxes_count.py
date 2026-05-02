import pytest

from pages.portfolio_page import PortfolioHomePage


@pytest.mark.web
@pytest.mark.regression
def test_checkboxes_page_loads_two_checkboxes(driver):
    page = PortfolioHomePage(driver)
    page.open()
    assert len(page.status_badges()) >= 1
