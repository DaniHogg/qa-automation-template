from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.config import settings
from pages.base_page import BasePage


class PortfolioHomePage(BasePage):
    TITLE = (By.TAG_NAME, "h1")
    LEDE = (By.CSS_SELECTOR, ".lede")
    PROJECT_CARDS = (By.CSS_SELECTOR, "#project-cards .card")
    STATUS_BADGES = (By.CSS_SELECTOR, "#project-cards .status")
    STALE_LABELS = (By.CSS_SELECTOR, "#project-cards .stale")
    DETAIL_LINKS = (By.CSS_SELECTOR, "#project-cards a[href*='project.html?project=']")
    WORKFLOW_LINKS = (By.CSS_SELECTOR, "#project-cards a[target='_blank']")

    def open(self):
        super().open(settings.base_url)

    def heading_text(self) -> str:
        return self.text_of(self.TITLE)

    def lede_text(self) -> str:
        return self.text_of(self.LEDE)

    def project_cards(self):
        self.wait.until(EC.presence_of_all_elements_located(self.PROJECT_CARDS))
        return self.driver.find_elements(*self.PROJECT_CARDS)

    def status_badges(self):
        self.wait.until(EC.presence_of_all_elements_located(self.STATUS_BADGES))
        return self.driver.find_elements(*self.STATUS_BADGES)

    def stale_labels(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#project-cards .card")))
        return self.driver.find_elements(*self.STALE_LABELS)

    def detail_links(self):
        self.wait.until(EC.presence_of_all_elements_located(self.DETAIL_LINKS))
        return self.driver.find_elements(*self.DETAIL_LINKS)

    def workflow_links(self):
        self.wait.until(EC.presence_of_all_elements_located(self.WORKFLOW_LINKS))
        return self.driver.find_elements(*self.WORKFLOW_LINKS)

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
