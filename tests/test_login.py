import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.loggers import get_logger

logger = get_logger()


@pytest.mark.smoke
def test_valid_login(page):
    """
    Smoke test: Verify login works with valid credentials
    """
    home = HomePage(page)
    login = LoginPage(page)

    logger.info("Opening homepage")
    home.open_homepage()

    logger.info("Navigating to Form Authentication page")
    home.click_form_authentication()

    logger.info("Logging in with valid credentials")
    login.login("tomsmith", "SuperSecretPassword!")

    flash_message = login.get_flash_message()
    logger.info(f"Flash message: {flash_message}")

    assert "You logged into a secure area!" in flash_message


@pytest.mark.regression
def test_invalid_login(page):
    """
    Regression test: Verify login fails with invalid credentials
    """
    home = HomePage(page)
    login = LoginPage(page)

    logger.info("Opening homepage")
    home.open_homepage()

    logger.info("Navigating to Form Authentication page")
    home.click_form_authentication()

    logger.info("Logging in with invalid credentials")
    login.login("wronguser", "wrongpass")
    # login.login("tomsmith", "SuperSecretPassword!")


    flash_message = login.get_flash_message()
    logger.info(f"Flash message: {flash_message}")

    assert "Your username is invalid!" in flash_message
