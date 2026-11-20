import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import SITE_URL
from helpers import generate_email, generate_password
from locators import HomeLocators, LoginLocators, RegistrationLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def register_user(driver):
    email = generate_email()
    password = generate_password()
    name = "Ирина"

    driver.get(f"{SITE_URL}register")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 20).until(EC.url_to_be(f"{SITE_URL}login"))

    return email, password


@pytest.fixture
def register_and_login(driver, register_user):
    email, password = register_user

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(HomeLocators.ORDER_BUTTON))
