import pytest

from pages.dynamic_loading_page import DynamicLoadingPage


@pytest.mark.web
@pytest.mark.regression
def test_dynamic_loading_reveals_finish_text(driver):
    page = DynamicLoadingPage(driver)
    page.open()
    page.start()
    assert page.finish_text() == "Hello World!"
