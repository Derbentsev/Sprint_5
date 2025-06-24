from tests.data import data
from tests.data import locators
from tests.data import urls

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationUser:
    def test_registration_success(self, driver, fill_registration_form_factory):
        driver.get(urls.url_register_page())

        fill_registration_form_factory(driver, data.user_name(), data.user_email(), data.user_password())

        element = WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                locators.locator_login_user_enter_button_registration_form()
            )
        )

        assert element.is_displayed()


    def test_registration_password_small_failed(self, driver, fill_registration_form_factory):
        user_password_wrong = '123'
        driver.get(urls.url_register_page())
        
        fill_registration_form_factory(driver, data.user_name(), data.user_email(), user_password_wrong)
        element = driver.find_element(*locators.locator_wrong_password_text())
        assert element.is_displayed()
