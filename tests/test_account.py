from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import SITE_URL
from locators import AccountLocators, HeaderLocators, HomeLocators, LoginLocators


class TestPersonalAccount:

    def test_open_personal_account(self, driver, register_and_login):

        driver.find_element(*HeaderLocators.ACCOUNT_LINK).click()

        WebDriverWait(driver, 20).until(EC.url_contains("/account"))
        profile = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountLocators.PROFILE_LINK))
        assert profile.is_displayed()

    def test_return_to_constructor_by_button(self, driver, register_and_login):
        driver.find_element(*HeaderLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 20).until(EC.url_contains("/account"))

        driver.find_element(*HeaderLocators.CONSTRUCTOR_LINK).click()

        title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomeLocators.TITLE))
        assert title.is_displayed()
        assert driver.current_url == SITE_URL

    def test_return_to_constructor_by_logo(self, driver, register_and_login):
        driver.find_element(*HeaderLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 20).until(EC.url_contains("/account"))

        driver.find_element(*HeaderLocators.LOGO).click()

        title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HomeLocators.TITLE)
        )
        assert title.is_displayed()
        assert driver.current_url == SITE_URL

    def test_logout(self, driver, register_and_login):
        driver.find_element(*HeaderLocators.ACCOUNT_LINK).click()

        logout_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(AccountLocators.LOGOUT_BUTTON))
        logout_button.click()

        WebDriverWait(driver, 20).until(EC.url_to_be(f"{SITE_URL}login"))
        assert driver.find_element(*LoginLocators.TITLE).is_displayed()
