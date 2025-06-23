import pytest

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
    driver.get('https://stellarburgers.nomoreparties.site')

    WebDriverWait(driver, 7).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//p[text()="Личный Кабинет"]')
        )
    )

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//p[text()="Конструктор"]')
        )
    ).click()

    try:
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//h1[text()="Соберите бургер"]')
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
    driver.get('https://stellarburgers.nomoreparties.site')

    assert enter_section(driver, section)


def test_enter_constructor_via_click_logo_success():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')

    try:
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[class*=AppHeader_header__logo__]')
            )
        ).click()

        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//h1[text()="Соберите бургер"]')
            )
        )

        assert True
    except:
        assert False
    finally:
        driver.quit()
