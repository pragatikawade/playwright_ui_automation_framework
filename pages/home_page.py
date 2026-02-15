from pages.base_page import BasePage

class HomePage(BasePage):
    """
    HomePage class represents the homepage of
    'the-internet.herokuapp.com' website.
    """

    def open_homepage(self):
        """
        Open the homepage URL.
        """
        self.navigate("https://the-internet.herokuapp.com/")

    def get_homepage_title(self):
        """
        Get the title of the homepage.

        Returns:
            str: The homepage title
        """
        return self.get_title()

    def click_form_authentication(self):
        """
        Click the 'Form Authentication' link on homepage.
        """
        # Playwright clicks the link containing text
        self.page.click("text=Form Authentication")
