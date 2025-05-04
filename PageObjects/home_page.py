from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.homePage_locator import HomePage_Locator

class HomePage(BasePage):
    HOMEPAGE_LOGIN_BUTTON = (By.ID, HomePage_Locator.homepage_login_button)

    def click_homepage_login(self):
        self.click(self.HOMEPAGE_LOGIN_BUTTON)