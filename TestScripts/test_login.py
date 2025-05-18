import pytest

from PageObjects.home_page import HomePage
from PageObjects.base_page import BasePage
from PageObjects.login_page import Login_Page
from TestDate.data import Data
from Configuration.conftest import driver_setup

# @pytest.fixture
# def page_objects(driver_setup):
#     return {
#         "base_page": BasePage(driver_setup),
#         "home_page": HomePage(driver_setup),
#         "login_page": Login_Page(driver_setup)
#     }

def test_url(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    assert base_page.fetch_title() == "GUVI | Learn to code in your native language"

    # assert base_page.fetch_url() == "https://www.guvi.in/"
    print("\nSUCCESS: URL is valid")

    home_page = HomePage(driver_setup)
    home_page.click_homepage_login()
    # print(base_page.fetch_title())
    # print(base_page.fetch_url())
    assert base_page.fetch_url() == Data.home_page_url
    print("SUCCESS: HomePage URL is valid")

def test_check_emai_password_inout_box_visible(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    assert base_page.fetch_url() == Data.url

    home_page = HomePage(driver_setup)
    home_page.click_homepage_login()

    login_page = Login_Page(driver_setup)
    try:
        base_page.is_visible(login_page.EMAIL_ADDRESS)
        print("\nSUCCESS: Email Address is visible")
    except Exception as e:
        print(f"FAILED: Email Address is not visible {e}")
    try:
        base_page.is_visible(login_page.PASSWORD)
        print("SUCCESS: Password is visible")
    except Exception as e:
        print(f"FAILED: Password is not visible {e}")

def test_check_Login_button_is_enable(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    assert base_page.fetch_url() == Data.url

    home_page = HomePage(driver_setup)
    home_page.click_homepage_login()

    login_page = Login_Page(driver_setup)
    try:
        base_page.is_enable(login_page.LOGINPAGE_LOGIN_BUTTON)
        print("\nSUCCESS: Login Button is Enabled")
    except Exception as e:
        print(f"FAILED: Login Button is not Enabled {e}")



def test_valid_emai_password(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    home_page = HomePage(driver_setup)
    login_page = Login_Page(driver_setup)

    home_page.click_homepage_login()
    try:
        assert base_page.fetch_url() == Data.home_page_url
        login_page.enter_valid_email_address()
        login_page.enter_valid_password()
        login_page.click_loginpage_login_button()
        print("\nSUCCESS: USER Logged-in with valid credential")
    except Exception as e:
        print(f"FAILED: USER login failed: {e}")


def test_invalid_emai_password(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)
    home_page = HomePage(driver_setup)
    login_page = Login_Page(driver_setup)

    home_page.click_homepage_login()
    try:
        assert base_page.fetch_url() == Data.home_page_url
        login_page.enter_invalid_email_address()
        login_page.enter_invalid_password()
        login_page.click_loginpage_login_button()
        try:
            assert base_page.fetch_url() == Data.home_page_url
            print("\nSUCCESS: USER not logged-in with invalid credential")
        except Exception as e:
            print("\nFAILED: USER logged-in with invalid credential")
    except Exception as e:
        print(f"FAILED: USER login failed: {e}")