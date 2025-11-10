import pytest
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="uat", help="Environment: uat/parallel")
    parser.addoption("--targetbrowser", action="store", default="chromium", help="Browser: chromium/edge/webkit")
    

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    config_path=Path(f"config/{env}.json")
    print(config_path)
    with open(config_path) as f:
        return json.load(f)
    

@pytest.fixture(scope="session")
def browser_context(request):
    browser_name=request.config.getoption("--browser")
    headed = request.config.getoption("--headed")
    with sync_playwright() as p:
        if browser_name=="edge":
            browser = p.chromium.launch(channel="msedge", headless=not headed)
        else:
            browser = getattr(p,browser_name).launch(headless=False)

        context=browser.new_context()
        yield context
        context.close()
        browser.close()

    @pytest.fixture
    def page(browser_context):
        page = browser_context.new_page()
        yield page
        page.close()