import pytest
from tests.data import locators
from tests.data import urls

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSectionConstructor:
    def test_enter_section_constructor_via_personal_account_success(self, driver, enter_section_factory):
        driver.get(urls.url_login_account())

        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable(
                locators.locator_constructor_text()
            )
        ).click()

        element = WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                locators.locator_create_burger_text()
            )
        )

        assert element.is_displayed()


    @pytest.mark.parametrize('section', ['Булки', 'Соусы', 'Начинки'])
    def test_enter_section_success(self, driver, section, enter_section_factory):
        driver.get(urls.url_main_page())
        assert enter_section_factory(driver, section)


    def test_enter_constructor_via_click_logo_success(self, driver):
        driver.get(urls.url_login_page())

        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                locators.locator_logo_text()
            )
        ).click()

        element = WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                locators.locator_create_burger_text()
            )
        )

        assert element.is_displayed()
