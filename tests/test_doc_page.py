from pages.docs_page import DocsPage
from playwright.sync_api import expect
import pytest


@pytest.mark.smoke
def test_main_page(page):
    page = DocsPage(page)
    page.open_page()
    expect(page.getting_started_link).to_be_visible()
