from PageObjects.home_page import HomePage
from PageObjects.base_page import BasePage
from TestDate.data import Data
from Configuration.confTest import driver_setup

def test_url(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)

    assert base_page.fetch_title() == "GUVI | Learn to code in your native language"

    # assert base_page.fetch_url() == "https://www.guvi.in/"
    print("SUCCESS: URL is valid")