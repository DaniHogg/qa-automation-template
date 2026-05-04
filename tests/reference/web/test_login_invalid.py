import pytest

from core.config import settings
from pages.portfolio_page import PortfolioHomePage
from tests.reference.web.assertions import assert_text_matches_keywords


@pytest.mark.web
@pytest.mark.regression
def test_home_lede_explains_dashboard_scope(driver):
    page = PortfolioHomePage(driver)
    page.open()
    assert_text_matches_keywords(
        page.lede_text(),
        settings.web_contract.lede_keywords,
        label="dashboard lede",
    )
