import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# This Driver setup is common for all the test
@pytest.fixture()
def driver_setup():
    # initialize the driver setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # teardown method
    driver.quit()
