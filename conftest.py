import random
import string

import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import HomeLocators, LoginLocators, RegistrationLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def generate_email():
    name = "irina"
    surname = "khlamova"
    cohort = "56"
    random_numbers = random.randint(100, 999)
    email = f"{name}{surname}{cohort}{random_numbers}@yandex.ru"
    return email


@pytest.fixture
def generate_password():
    def func(length=6):
        characters = string.ascii_letters + string.digits
        password = "".join(random.choices(characters, k=length))
        return password
    return func


@pytest.fixture
def register_user(driver, generate_email, generate_password):
    email = generate_email
    password = generate_password()
    name = "Ирина"

    driver.get("https://stellarburgers.education-services.ru/register")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT))

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))

    return email, password


@pytest.fixture
def register_and_login(driver, register_user):
    email, password = register_user

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(HomeLocators.ORDER_BUTTON))
