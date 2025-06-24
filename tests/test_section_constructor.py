import pytest
from tests.data import locators
from tests.data import urls

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def enter_section(driver, section_name):
    try:
        element = WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, f'//span[text()="{section_name}"]')
            )
        )
        driver.execute_script('arguments[0].click()', element)

        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, f'//h2[text()="{section_name}"]')
            )
        )

        return True
    except Exception as e:
        print(str(e))
        return False


def test_enter_section_constructor_via_personal_account_success(chrome_driver):
    driver = chrome_driver
    driver.get(urls.url_main_page)

    WebDriverWait(driver, 7).until(
        expected_conditions.visibility_of_element_located(
            *locators.locator_personal_account_button
        )
    )

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            *locators.locator_constructor_text
        )
    ).click()

    try:
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                *locators.locator_create_burger_text
            )
        )

        assert enter_section
    except:
        assert False
    finally:
        driver.quit()


@pytest.mark.parametrize('section', ['Булки', 'Соусы', 'Начинки'])
def test_enter_section_success(chrome_driver, section):
    driver = chrome_driver
    driver.get(urls.url_main_page)

    assert enter_section(driver, section)


def test_enter_constructor_via_click_logo_success():
    driver = webdriver.Chrome()
    driver.get(urls.url_login_page)

    try:
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                *locators.locator_logo_text
            )
        ).click()

        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                *locators.locator_create_burger_text
            )
        )

        assert True
    except:
        assert False
    finally:
        driver.quit()
