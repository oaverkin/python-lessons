from playwright.sync_api import Page

from pages.base_page import BasePage


class DocsPage(BasePage):
    page_url = "/python/docs/intro"

    def __init__(self, page: Page):
        super().__init__(page)
