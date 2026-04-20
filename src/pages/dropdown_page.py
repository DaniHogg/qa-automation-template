from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from core.config import settings
from pages.base_page import BasePage


class DropdownPage(BasePage):
    """Dropdown page of the-internet.herokuapp.com"""

    DROPDOWN = (By.ID, "dropdown")

    def open(self):
        super().open(f"{settings.base_url}/dropdown")

    def select_by_value(self, value: str):
        element = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN))
        Select(element).select_by_value(value)

    def selected_option_text(self) -> str:
        element = self.wait.until(EC.presence_of_element_located(self.DROPDOWN))
        return Select(element).first_selected_option.text

    def all_option_texts(self) -> list[str]:
        element = self.wait.until(EC.presence_of_element_located(self.DROPDOWN))
        return [o.text for o in Select(element).options]
