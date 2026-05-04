import pytest
from selenium.webdriver.common.by import By

from pages.portfolio_page import PortfolioHomePage


@pytest.mark.web
@pytest.mark.regression
def test_detail_back_link_returns_to_dashboard(driver):
    home = PortfolioHomePage(driver)
    home.open()
    home.open_first_project_detail()

    driver.find_element(By.CSS_SELECTOR, ".back-link").click()
    assert "dashboard.html" in driver.current_url
