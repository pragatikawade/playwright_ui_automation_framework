import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_homepage_title(page):
    """
    Smoke test to verify homepage title contains 'The Internet'.
    """
    home = HomePage(page)

    # Open homepage
    home.open_homepage()

    # Get page title
    title = home.get_homepage_title()
    print("Page Title:", title)  # Optional debug output

    # Assertion to verify title contains expected text
    assert "The Internet" in title


def test_navigate_to_login(page):
    """
    Test to verify navigation to 'Form Authentication' page.
    """
    home = HomePage(page)

    # Open homepage
    home.open_homepage()

    # Click the Form Authentication link
    home.click_form_authentication()

    # Assert that URL now contains /login
    assert "/login" in page.url
