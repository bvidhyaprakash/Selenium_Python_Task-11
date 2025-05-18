from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.loginpage_locator import LoginPage_Locators
from TestDate.data import Data


class Login_Page(BasePage):
    EMAIL_ADDRESS = (By.ID, LoginPage_Locators.username_locator)
    PASSWORD = (By.ID, LoginPage_Locators.password_locator)
    LOGINPAGE_LOGIN_BUTTON = (By.ID, LoginPage_Locators.login_button_locator)


    def enter_valid_email_address(self):
        self.enter_text(self.EMAIL_ADDRESS, Data.username)

    def enter_valid_password(self):
        self.enter_text(self.PASSWORD, Data.password)

    def enter_invalid_email_address(self):
        self.enter_text(self.EMAIL_ADDRESS, Data.invalid_username)

    def enter_invalid_password(self):
        self.enter_text(self.PASSWORD, Data.invalid_password)

    def click_loginpage_login_button(self):
        self.click(self.LOGINPAGE_LOGIN_BUTTON)