from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

from Configuration.confTest import driver_setup


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15


    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_test(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def fetch_title(self):
        try:
            title = self.driver.title
            return title
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

    def fetch_url(self):
        try:
            return self.driver.url
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)
