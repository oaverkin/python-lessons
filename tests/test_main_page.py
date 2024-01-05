from pages.main_page import MainPage
from playwright.sync_api import expect
import pytest


@pytest.mark.smoke
def test_main_page(page):
    page = MainPage(page)
    page.open_page()
    expect(page.docs_link).to_be_visible()
    expect(page.community_link).to_be_visible()
    expect(page.get_started_link).to_be_visible()
