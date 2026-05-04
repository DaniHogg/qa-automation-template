import pytest

from core.config import settings
from pages.portfolio_page import PortfolioHomePage
from tests.reference.web.assertions import assert_text_matches_keywords


@pytest.mark.web
@pytest.mark.smoke
def test_home_page_has_heading(driver):
    page = PortfolioHomePage(driver)
    page.open()
    assert_text_matches_keywords(
        page.heading_text(),
        settings.web_contract.heading_keywords,
        label="dashboard heading",
    )
