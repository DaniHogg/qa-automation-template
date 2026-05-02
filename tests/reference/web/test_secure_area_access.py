import pytest

from pages.portfolio_page import PortfolioHomePage, PortfolioProjectPage


@pytest.mark.web
@pytest.mark.regression
def test_project_detail_shows_suite_rows(driver):
    home = PortfolioHomePage(driver)
    home.open()
    home.open_first_project_detail()

    detail = PortfolioProjectPage(driver)
    assert len(detail.suite_rows()) >= 1
