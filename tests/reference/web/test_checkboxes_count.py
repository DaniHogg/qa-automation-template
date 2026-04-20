import pytest

from pages.checkboxes_page import CheckboxesPage


@pytest.mark.web
@pytest.mark.regression
def test_checkboxes_page_loads_two_checkboxes(driver):
    page = CheckboxesPage(driver)
    page.open()
    assert len(page.checkboxes()) == 2
