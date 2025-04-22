import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Locators, Urls, Data

class TestLogIn:

    @pytest.mark.parametrize(
        "pages, locators",
        [
            (Urls.MAIN_PAGE, Locators.MAIN_PAGE_LOG_IN_BUTTON),
            (Urls.LOGIN_PAGE, Locators.ACCOUNT_BUTTON),
            (Urls.REGISTRATION_PAGE, Locators.ENTER_FROM_REGISTRATION_PAGE_BUTTON_FORGOT_PASSWORD),
            (Urls.FORGOT_PASSWORD_PAGE, Locators.ENTER_FROM_REGISTRATION_PAGE_BUTTON_FORGOT_PASSWORD),
        ],
        ids=(
            "main",
            "account",
            "registration",
            "forgot-password",
        ),
    )
    def test_log_in_from_forgot_pwd_page(self, pages, locators, driver):
        driver.get(pages)

        driver.find_element(*locators).click()

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.LOGIN)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, timeout=3).until(
            expected_conditions.visibility_of_element_located(
                (Locators.ORDER_BUTTON)
            )
        )