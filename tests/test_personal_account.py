from tests.data import data
from tests.data import locators
from tests.data import urls

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def register_user(driver, user_email, user_password):
    driver.find_element(*locators.locator_login_user_email).send_keys(user_email)
    
    driver.find_element(*locators.locator_login_user_password).send_keys(user_password)

    driver.find_element(*locators.locator_login_user_enter_button).click()

    # Здесь я проверяю, что мы действительно зашли в ЛК
    # Иначе я не нашел каких-то признаков в интерфейсе, что мы зашли в Профиль
    try:
        driver.find_element(*locators.locator_personal_account_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                *By.XPATH, locators.locator_personal_profile_text
            )
        )

        return True
    except:
        return False


def test_login_via_enter_account_success():
    driver = webdriver.Chrome()
    driver.get(urls.url_main_page)

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            *locators.locator_login_user_enter_account_button
        )
    ).click()

    try:
        assert register_user(driver, data.user_email, data.user_password)
    except:
        assert False
    finally:
        driver.quit()


def test_login_via_personal_account_click_success():
    driver = webdriver.Chrome()
    driver.get(urls.url_main_page)

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            *locators.locator_personal_account_button
        )
    ).click()

    try:
        assert register_user(driver, data.user_email, data.user_password)
    except:
        assert False
    finally:
        driver.quit()


def test_login_via_registration_form_success():
    driver = webdriver.Chrome()
    driver.get(urls.url_register_page)

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            *locators.locator_login_user_enter_button
        )
    ).click()

    try:
        assert register_user(driver, data.user_email, data.user_password)
    except:
        assert False
    finally:
        driver.quit()


def test_login_via_recover_password_success():
    driver = webdriver.Chrome()
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

    try:
        assert register_user(driver, data.user_email, data.user_password)
    except:
        assert False
    finally:
        driver.quit()


def test_logout_via_press_exit_button_success():
    driver = webdriver.Chrome()
    driver.get(urls.url_main_page)

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            *locators.locator_personal_account_button
        )
    ).click()

    register_user(driver, data.user_email, data.user_password)

    try:
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
    except:
        assert False
    finally:
        driver.quit()
