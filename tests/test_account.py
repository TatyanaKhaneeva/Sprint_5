import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Locators, Urls, Data

class TestAccount:
    def test_account_open_from_main_page(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.MAIN_PAGE_LOG_IN_BUTTON).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.PROFILE_BUTTON)
            )
        )


    @pytest.mark.parametrize(
        "buttons",
        (
            Locators.CONSTRUCTOR_BUTTON,
            Locators.LOGO,
        ),
        ids=(
            "by_designer",
            "by_logo",
        ),
    )
    def test_account_redirect_to_main_page(self, buttons, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.MAIN_PAGE_LOG_IN_BUTTON).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        driver.find_element(*buttons).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.MAKE_BURGER_TEXT)
            )
        )


    def test_account_log_out(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*Locators.MAIN_PAGE_LOG_IN_BUTTON).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.EXIT_BUTTON)
            )
        )
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.ENTER_BUTTON)
            )
        )