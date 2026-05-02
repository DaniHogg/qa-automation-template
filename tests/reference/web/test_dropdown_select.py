import pytest

from pages.portfolio_page import PortfolioHomePage, PortfolioProjectPage


@pytest.mark.web
@pytest.mark.regression
def test_dropdown_select_option_1(driver):
    home = PortfolioHomePage(driver)
    home.open()
    home.open_first_project_detail()

    detail = PortfolioProjectPage(driver)
    history_count = len(detail.history_rows())
    assert 1 <= history_count <= 5
