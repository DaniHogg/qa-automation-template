import pytest

from pages.checkboxes_page import CheckboxesPage


@pytest.mark.web
@pytest.mark.regression
def test_checkbox_can_be_toggled(driver):
    page = CheckboxesPage(driver)
    page.open()
    initial_state = page.is_checked(0)
    page.toggle(0)
    assert page.is_checked(0) != initial_state, "Checkbox state should change after toggle"
