import re
import time
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
import pytest

@pytest.mark.smoke

def test_homepage_title():
    with sync_playwright() as p:


        browser = p.chromium.launch(headless=False)
        #EDGE_PATH = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        #browser = p.chromium.launch(headless=False,executable_path=EDGE_PATH)

        page = browser.new_page()

        page.goto("https://starsbranchcouat.bmv.in.gov/BMVWebApp/Customer/QueueManagement.aspx")

        print("Title:", page.title())
        time.sleep(2)

        page.get_by_role("link", name="Customer Search").click()
        time.sleep(2)

        page.get_by_role("button", name="Search").click()
        time.sleep(2)
        
        page.get_by_text("CS-1435: Search contains").click()
        expect(page.get_by_role("listitem")).to_contain_text("CS-1435: Search contains invalid search criteria.")


        browser.close()
