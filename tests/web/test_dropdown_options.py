import pytest

from pages.dropdown_page import DropdownPage


@pytest.mark.web
@pytest.mark.regression
def test_dropdown_has_expected_options(driver):
    page = DropdownPage(driver)
    page.open()
    options = page.all_option_texts()
    assert "Option 1" in options
    assert "Option 2" in options
