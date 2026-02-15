import pytest
from pages.home_page import HomePage
from utils.loggers import get_logger

logger = get_logger()  # Initialize logger

@pytest.mark.smoke
def test_homepage_title(page):
    """
    Smoke test to verify homepage title contains 'The Internet'.
    """
    home = HomePage(page)

    logger.info("Opening homepage")
    home.open_homepage()

    title = home.get_homepage_title()
    logger.info(f"Homepage title: {title}")

    assert "The Internet" in title
    logger.info("Homepage title verified successfully")


def test_navigate_to_login(page):
    """
    Test to verify navigation to 'Form Authentication' page.
    """
    home = HomePage(page)

    logger.info("Opening homepage")
    home.open_homepage()

    logger.info("Clicking Form Authentication link")
    home.click_form_authentication()

    assert "/login" in page.url
    logger.info("Navigation to login page verified successfully")
