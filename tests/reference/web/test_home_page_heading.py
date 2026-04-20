import pytest

from pages.example_page import ExamplePage


@pytest.mark.web
@pytest.mark.smoke
def test_home_page_has_heading(driver):
    page = ExamplePage(driver)
    page.open_home()
    assert page.heading_text(), "Expected non-empty page heading"
