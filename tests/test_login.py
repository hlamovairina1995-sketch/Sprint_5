from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import SITE_URL
from locators import HeaderLocators, HomeLocators, LoginLocators, RecoveryLocators, RegistrationLocators


class TestLogin:

    def test_login_from_home(self, driver, register_user):

        email, password = register_user

        driver.get(SITE_URL)
        driver.find_element(*HomeLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginLocators.TITLE))

        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

        order_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(HomeLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_personal_account(self, driver, register_user):

        email, password = register_user

        driver.get(SITE_URL)
        driver.find_element(*HeaderLocators.ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginLocators.TITLE))

        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

        order_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(HomeLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_registration(self, driver, register_user):

        email, password = register_user

        driver.get(f"{SITE_URL}register")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.TITLE))
        driver.find_element(*RegistrationLocators.LOGIN_LINK).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginLocators.TITLE))

        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

        order_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(HomeLocators.ORDER_BUTTON))
        assert order_button.is_displayed()

    def test_login_from_password_recovery(self, driver, register_user):

        email, password = register_user

        driver.get(f"{SITE_URL}forgot-password")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RecoveryLocators.TITLE))
        driver.find_element(*RecoveryLocators.LOGIN_LINK).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginLocators.TITLE))

        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

        order_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(HomeLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
