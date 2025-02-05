from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Locators, Urls, Data, Errors

class TestRegistration:

    def test_registration_user_already_exists(self, driver):
        driver.get(Urls.REGISTRATION_PAGE)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        driver.find_element(*Locators.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.REGISTRATION_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.text_to_be_present_in_element(
                (Locators.ERROR_VALIDATION), Errors.USER_ALREADY_EXIST
            )
        )

    def test_registration_user_pwd_len_err(self, driver):
        driver.get(Urls.REGISTRATION_PAGE)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        driver.find_element(*Locators.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.REGISTRATION_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.SHORT_PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.text_to_be_present_in_element(
                (Locators.ERROR_VALIDATION), Errors.WRONG_PASSWORD
            )
        )