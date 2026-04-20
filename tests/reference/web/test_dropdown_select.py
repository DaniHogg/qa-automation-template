import pytest

from pages.dropdown_page import DropdownPage


@pytest.mark.web
@pytest.mark.regression
def test_dropdown_select_option_1(driver):
    page = DropdownPage(driver)
    page.open()
    page.select_by_value("1")
    assert page.selected_option_text() == "Option 1"
