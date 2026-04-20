import pytest

from pages.example_page import ExamplePage


@pytest.mark.web
@pytest.mark.smoke
def test_home_page_lists_examples(driver):
    page = ExamplePage(driver)
    page.open_home()
    examples = page.available_examples()
    assert len(examples) >= 10, "Expected at least 10 example links on home page"
