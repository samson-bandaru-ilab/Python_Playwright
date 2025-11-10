from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import time

class QueueManagementPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.queue_mgmt_header = page.get_by_text("Queue Management")
        time.sleep(2)

    def is_page_visible(self):
        expect(self.queue_mgmt_header).to_be_visible()

        return self.queue_mgmt_header.is_visible()
    
    def select_left_nav(self, link:str):
        self.page.get_by_role("link", name=link).click()