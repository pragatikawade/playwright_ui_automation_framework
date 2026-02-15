import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime


@pytest.fixture(scope="function")
def page():
    """
    Pytest fixture to launch browser and provide
    Playwright page object to tests.

    Yields:
        playwright.sync_api._generated.Page: Playwright page object
    """
    with sync_playwright() as p:
        # Launch Chrome browser
        browser = p.chromium.launch(
            channel="chrome",  # Use installed Google Chrome
            headless=False  # Set True to run in background
        )

        # Open new browser tab
        page = browser.new_page()

        # Provide page to the test
        yield page

        # Close browser after test
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot on test failure
    if report.when == "call" and report.failed:

        page = item.funcargs.get("page", None)
        if page:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            file_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"

            page.screenshot(path=file_path)
            print(f"\nScreenshot saved: {file_path}")