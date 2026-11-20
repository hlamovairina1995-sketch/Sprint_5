from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import SITE_URL
from locators import ConstructorLocators, HomeLocators


class TestConstructor:

    def test_buns_tab(self, driver):
        driver.get(SITE_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomeLocators.TITLE))

        driver.find_element(*ConstructorLocators.SAUCES_TAB).click()
        driver.find_element(*ConstructorLocators.BUNS_TAB).click()

        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.BUNS_ACTIVE))
        assert active_tab.is_displayed()

    def test_sauces_tab(self, driver):
        driver.get(SITE_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomeLocators.TITLE))

        driver.find_element(*ConstructorLocators.SAUCES_TAB).click()

        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.SAUCES_ACTIVE))
        assert active_tab.is_displayed()

    def test_fillings_tab(self, driver):
        driver.get(SITE_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomeLocators.TITLE))

        driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()

        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.FILLINGS_ACTIVE))
        assert active_tab.is_displayed()

