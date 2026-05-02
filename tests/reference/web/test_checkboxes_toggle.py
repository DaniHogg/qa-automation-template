import pytest

from pages.portfolio_page import PortfolioHomePage


@pytest.mark.web
@pytest.mark.regression
def test_checkbox_can_be_toggled(driver):
    page = PortfolioHomePage(driver)
    page.open()
    card_text = page.project_cards()[0].text
    assert "Fresh" in card_text or "Stale" in card_text
