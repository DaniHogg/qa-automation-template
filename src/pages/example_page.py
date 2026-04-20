from selenium.webdriver.common.by import By

from core.config import settings
from pages.base_page import BasePage


class HomePage(BasePage):
    """Landing page of the-internet.herokuapp.com"""

    HEADING = (By.TAG_NAME, "h1")
    LINKS = (By.CSS_SELECTOR, "ul li a")

    def open(self, url: str | None = None):
        super().open(url or settings.base_url)

    def heading_text(self) -> str:
        return self.text_of(self.HEADING)

    def available_examples(self) -> list[str]:
        from selenium.webdriver.support import expected_conditions as EC
        elements = self.wait.until(EC.presence_of_all_elements_located(self.LINKS))
        return [el.text for el in elements if el.text]


class LoginPage(BasePage):
    """Form Authentication page of the-internet.herokuapp.com"""

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def open(self):
        super().open(f"{settings.base_url}/login")

    def login(self, username: str, password: str):
        self.wait_and_type(self.USERNAME_INPUT, username)
        self.wait_and_type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def flash_text(self) -> str:
        return self.text_of(self.FLASH_MESSAGE)


# Keep backward-compatible alias used by the existing smoke test
class ExamplePage(HomePage):
    def open_home(self):
        self.open()
