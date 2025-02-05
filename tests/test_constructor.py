from constants import Locators, Urls

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
        driver.find_element(*Locators.BUNS_BUTTON).click()
        current_class = driver.find_element(*Locators.BUNS_BUTTON).get_attribute('class')
        assert "tab_tab_type_current" in current_class