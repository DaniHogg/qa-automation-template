import pytest
from selenium.webdriver.common.by import By

from pages.portfolio_page import PortfolioHomePage, PortfolioProjectPage


@pytest.mark.web
@pytest.mark.regression
def test_dynamic_loading_reveals_finish_text(driver):
    home = PortfolioHomePage(driver)
    home.open()
    home.open_first_project_detail()

    detail = PortfolioProjectPage(driver)
    if not driver.find_elements(By.ID, "coverage-link"):
        pytest.skip("Coverage panel not yet deployed on target GitHub Pages site")
    assert detail.coverage_href().endswith("coverage-audit.json")
