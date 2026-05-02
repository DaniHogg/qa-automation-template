import pytest

from pages.portfolio_page import PortfolioHomePage, PortfolioProjectPage


@pytest.mark.web
@pytest.mark.regression
def test_project_detail_opens_from_card(driver):
    home = PortfolioHomePage(driver)
    home.open()
    home.open_first_project_detail()

    detail = PortfolioProjectPage(driver)
    assert detail.title_text(), "Expected project detail title"
