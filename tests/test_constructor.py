from selenium.webdriver.support.wait import WebDriverWait
from constants import Locators, Urls
from selenium.webdriver.support import expected_conditions as EC

class TestDesigner:

    def test_designer_check_filling(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        current_class = driver.find_element(*Locators.FILLINGS_BUTTON).get_attribute('class')
        assert "tab_tab_type_current" in current_class

    def test_designer_check_sauce(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.SAUCES_BUTTON).click()
        current_class = driver.find_element(*Locators.SAUCES_BUTTON).get_attribute('class')
        assert "tab_tab_type_current" in current_class

    def test_designer_check_rolls(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.SAUCES_BUTTON).click()
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUNS_BUTTON))
        element.click()

        WebDriverWait(driver, 10).until(
            lambda d: "tab_tab_type_current" in d.find_element(*Locators.BUNS_BUTTON).get_attribute('class')
        )

        current_class = driver.find_element(*Locators.BUNS_BUTTON).get_attribute('class')
        assert "tab_tab_type_current" in current_class