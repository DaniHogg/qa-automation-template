import pytest

from core.config import settings
from pages.portfolio_page import PortfolioHomePage
from tests.reference.web.assertions import assert_text_matches_keywords


@pytest.mark.web
@pytest.mark.regression
def test_login_page_title(driver):
    page = PortfolioHomePage(driver)
    page.open()
    assert_text_matches_keywords(
        driver.title,
        settings.web_contract.title_keywords,
        label="dashboard title",
    )
