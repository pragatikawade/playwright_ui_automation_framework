from pages.home_page import HomePage

def test_navigate_to_login(page):
    home = HomePage(page)
    home.open_homepage()
    home.click_form_authentication()

    # Assert URL contains /login
    assert "/login" in page.url
