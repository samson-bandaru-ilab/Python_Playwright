from pages.base_page import BasePage
import time
from playwright.sync_api import Page, expect

class CustomerSearchPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.search_btn = page.get_by_role("button", name="Search")

        self.customer_search_header = page.get_by_text("Customer Search")

    def is_page_visible(self):
        expect(self.customer_search_header).to_be_visible()

        return self.customer_search_header.is_visible()

    def click_search(self):
        self.search_btn.click()
        time.sleep(2)
        
    def verify_error_message(self, error_msg:str):
       # self.page.get_by_text("CS-1435: Search contains").click()
       # expect(self.page.get_by_role("listitem")).to_contain_text("CS-1435: Search contains invalid search criteria.")
        expect(self.page.get_by_role("listitem")).to_contain_text(error_msg)

