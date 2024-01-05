import re

from playwright.sync_api import Page
from pages.base_page import BasePage


class MainPage(BasePage):
    page_url = "/python"

    def __init__(self, page: Page):
        super().__init__(page)

        self.get_started_link = page.get_by_role("link", name="Get started")
        self.community_link = page.get_by_role("link", name="Community")
        self.docs_link = page.get_by_role("link", name="Docs")
        self.title = page.get_by_title(re.compile("Playwright Python"))

    def click_get_started(self):
        self.get_started_link.click()

    def click_docs_link(self):
        self.docs_link.click()
