import pytest

from pages.portfolio_page import PortfolioHomePage, PortfolioProjectPage


@pytest.mark.web
@pytest.mark.regression
def test_dropdown_has_expected_options(driver):
    home = PortfolioHomePage(driver)
    home.open()
    home.open_first_project_detail()

    detail = PortfolioProjectPage(driver)
    assert len(detail.latest_meta_cards()) >= 4
