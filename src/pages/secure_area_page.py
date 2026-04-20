from selenium.webdriver.common.by import By

from core.config import settings
from pages.base_page import BasePage


class SecureAreaPage(BasePage):
    """Secure Area page reached after successful login on the-internet.herokuapp.com"""

    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    HEADING = (By.TAG_NAME, "h2")

    def heading_text(self) -> str:
        return self.text_of(self.HEADING)

    def flash_text(self) -> str:
        return self.text_of(self.FLASH_MESSAGE)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def is_on_secure_area(self) -> bool:
        return "/secure" in self.driver.current_url
