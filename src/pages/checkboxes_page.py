from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.config import settings
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    """Checkboxes page of the-internet.herokuapp.com"""

    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    def open(self):
        super().open(f"{settings.base_url}/checkboxes")

    def checkboxes(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.CHECKBOXES))

    def is_checked(self, index: int) -> bool:
        return self.checkboxes()[index].is_selected()

    def toggle(self, index: int):
        self.checkboxes()[index].click()
