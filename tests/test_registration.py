from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import SITE_URL
from helpers import generate_email, generate_password
from locators import LoginLocators, RegistrationLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password(6)
        name = "Ирина"

        driver.get(f"{SITE_URL}register")

        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

        assert driver.find_element(*RegistrationLocators.NAME_INPUT).get_attribute("value") != ""

        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 20).until(EC.url_to_be(f"{SITE_URL}login"))

        assert driver.find_element(*LoginLocators.TITLE).is_displayed()

    def test_registration_rejects_password_shorter_than_six(self, driver):
        email = generate_email()
        password = generate_password(5)
        name = "Ирина"

        driver.get(f"{SITE_URL}register")

        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))

        assert error.is_displayed()