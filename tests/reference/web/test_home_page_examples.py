import pytest

from pages.portfolio_page import PortfolioHomePage


@pytest.mark.web
@pytest.mark.smoke
def test_home_page_lists_examples(driver):
    page = PortfolioHomePage(driver)
    page.open()
    assert len(page.project_cards()) >= 1, "Expected at least one project card"
