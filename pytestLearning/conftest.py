import allure
import pytest
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright

@pytest.fixture(params=["chrome", "firefox"],scope="function")
def browser(request):
    browser_type = request.param
    with sync_playwright() as p:
        if browser_type == "chrome":
            browser = p.chromium.launch(headless=False)
        elif browser_type =="firefox":
            browser = p.firefox.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser: {browser_type}")
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    global page
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.close()

@pytest.fixture(autouse=True)
def setup_function(page):
    page.goto("http://facebook.com")

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(page.screenshot(path="screenshot/fullpage.png"), name="failuresreenshot",
                      attachment_type=AttachmentType.PNG)

