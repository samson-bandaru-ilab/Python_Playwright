from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url:str):
        self.page.goto(url)

    def click(self, locator:str):
        self.page.click(locator)

    def fill(self, locator:str, value:str):
        self.page.fill(locator, value)

    def get_text(self, locator:str):
        return self.page.inner_text(locator)