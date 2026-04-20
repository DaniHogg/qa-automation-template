from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config import settings
from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    """Dynamic Loading example 1 (hidden element) on the-internet.herokuapp.com"""

    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    FINISH_TEXT = (By.ID, "finish")

    def open(self):
        super().open(f"{settings.base_url}/dynamic_loading/1")

    def start(self):
        self.click(self.START_BUTTON)

    def finish_text(self, timeout: int = 15) -> str:
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.FINISH_TEXT)
        )
        return element.text
