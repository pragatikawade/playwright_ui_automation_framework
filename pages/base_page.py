class BasePage:
    """
    BasePage class contains generic browser actions
    that can be reused by all page objects.
    """

    def __init__(self, page):
        """
        Initialize BasePage with Playwright page object.

        Args:
            page (playwright.sync_api._generated.Page): Playwright page object
        """
        self.page = page

    def navigate(self, url):
        """
        Navigate to the given URL in the browser.

        Args:
            url (str): The URL to open
        """
        self.page.goto(url)

    def get_title(self):
        """
        Get the current page title.

        Returns:
            str: The title of the current page
        """
        return self.page.title()
