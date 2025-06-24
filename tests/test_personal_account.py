from tests.data import data
from tests.data import locators
from tests.data import urls

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:
    def test_login_via_enter_account_success(register_user_factory, chrome_driver):
        driver = chrome_driver
        driver.get(urls.url_main_page)

        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable(
                *locators.locator_login_user_enter_account_button
            )
        ).click()

        register_user_factory(driver, data.user_email, data.user_password)
        assert True


    def test_login_via_personal_account_click_success(register_user_factory, chrome_driver):
        driver = chrome_driver
        driver.get(urls.url_main_page)

        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable(
                *locators.locator_personal_account_button
            )
        ).click()

        register_user_factory(driver, data.user_email, data.user_password)
        assert True


    def test_login_via_registration_form_success(register_user_factory, chrome_driver):
        driver = chrome_driver
        driver.get(urls.url_register_page)

        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable(
                *locators.locator_login_user_enter_button
            )
        ).click()

        register_user_factory(driver, data.user_email, data.user_password)
        assert True


    def test_login_via_recover_password_success(register_user_factory, chrome_driver):
        driver = chrome_driver
        driver.get(urls.url_login_page)

        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable(
                *locators.locator_recover_password_link
            )
        ).click()

        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable(
                *locators.locator_login_user_enter_button
            )
        ).click()

        register_user_factory(driver, data.user_email, data.user_password)
        assert True


    def test_logout_via_press_exit_button_success(register_user_factory, chrome_driver):
        driver = chrome_driver
        driver.get(urls.url_main_page)

        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable(
                *locators.locator_personal_account_button
            )
        ).click()

        register_user_factory(driver, data.user_email, data.user_password)

        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                *locators.locator_exit_account_button
            )
        ).click()

        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                *locators.locator_login_user_enter_button
            )
        )
            
        assert True
