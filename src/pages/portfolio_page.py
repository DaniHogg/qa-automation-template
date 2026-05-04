from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin, urlparse

from core.config import settings
from pages.base_page import BasePage


class PortfolioHomePage(BasePage):
    TITLE = (By.TAG_NAME, "h1")
    LEDE = (By.CSS_SELECTOR, ".lede")

    def _project_cards_locator(self):
        container = settings.web_contract.project_cards_container_selector
        return (By.CSS_SELECTOR, f"{container} .card")

    def _status_badges_locator(self):
        container = settings.web_contract.project_cards_container_selector
        return (By.CSS_SELECTOR, f"{container} .status")

    def _stale_labels_locator(self):
        container = settings.web_contract.project_cards_container_selector
        return (By.CSS_SELECTOR, f"{container} .stale")

    def _detail_links_locator(self):
        container = settings.web_contract.project_cards_container_selector
        return (By.CSS_SELECTOR, f"{container} a[href*='project.html?project=']")

    def _workflow_links_locator(self):
        container = settings.web_contract.project_cards_container_selector
        return (By.CSS_SELECTOR, f"{container} a[target='_blank']")

    @staticmethod
    def _dashboard_url() -> str:
        base = settings.base_url
        path = urlparse(base).path.lower()
        dashboard_path = settings.web_contract.dashboard_path
        if path.endswith(dashboard_path.lower()):
            return base
        normalized = base if base.endswith("/") else f"{base}/"
        return urljoin(normalized, dashboard_path)

    def open(self):
        super().open(self._dashboard_url())

    def heading_text(self) -> str:
        return self.text_of(self.TITLE)

    def lede_text(self) -> str:
        return self.text_of(self.LEDE)

    def project_cards(self):
        locator = self._project_cards_locator()
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def status_badges(self):
        locator = self._status_badges_locator()
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def stale_labels(self):
        cards_locator = self._project_cards_locator()
        stale_locator = self._stale_labels_locator()
        self.wait.until(EC.presence_of_all_elements_located(cards_locator))
        return self.driver.find_elements(*stale_locator)

    def detail_links(self):
        locator = self._detail_links_locator()
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def workflow_links(self):
        locator = self._workflow_links_locator()
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def open_first_project_detail(self):
        self.detail_links()[0].click()


class PortfolioProjectPage(BasePage):
    TITLE = (By.ID, "project-title")
    META_CARDS = (By.CSS_SELECTOR, "#latest-meta .card")
    SUITE_ROWS = (By.CSS_SELECTOR, "#suite-rows tr")
    HISTORY_ROWS = (By.CSS_SELECTOR, "#history-list li")
    COVERAGE_CARDS = (By.CSS_SELECTOR, "#coverage-summary .card")
    COVERAGE_LINK = (By.ID, "coverage-link")

    def title_text(self) -> str:
        return self.text_of(self.TITLE)

    def latest_meta_cards(self):
        self.wait.until(EC.presence_of_all_elements_located(self.META_CARDS))
        return self.driver.find_elements(*self.META_CARDS)

    def suite_rows(self):
        self.wait.until(EC.presence_of_all_elements_located(self.SUITE_ROWS))
        return self.driver.find_elements(*self.SUITE_ROWS)

    def history_rows(self):
        self.wait.until(EC.presence_of_all_elements_located(self.HISTORY_ROWS))
        return self.driver.find_elements(*self.HISTORY_ROWS)

    def coverage_cards(self):
        self.wait.until(EC.presence_of_all_elements_located(self.COVERAGE_CARDS))
        return self.driver.find_elements(*self.COVERAGE_CARDS)

    def coverage_href(self) -> str:
        return self.wait.until(EC.presence_of_element_located(self.COVERAGE_LINK)).get_attribute("href")
