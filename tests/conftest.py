import pytest
from playwright.sync_api import sync_playwright


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
