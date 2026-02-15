from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Page object for Form Authentication page
    """
    def login(self, username, password):
        """
        Enter username and password and submit the form
        """
        self.page.fill("input#username", username)
        self.page.fill("input#password", password)
        self.page.click("button[type='submit']")

    def get_flash_message(self):
        """
        Return the flash message text after login attempt
        """
        return self.page.inner_text("#flash")
