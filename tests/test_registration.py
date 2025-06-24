from tests.data import data
from tests.data import locators
from tests.data import urls

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#Заполняем форму регистрации и логинимся
def fill_registration_form(driver, user_name, user_email, user_password):
    print(f'{user_email} : {user_password}')

    try:
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                *locators.locator_login_user_name)
        ).send_keys(user_name)
        
        driver.find_element(*locators.locator_login_user_email).send_keys(user_email)
        
        driver.find_element(*locators.locator_login_user_password).send_keys(user_password)

        driver.find_element(*locators.locator_register_button).click()
        
        return True
    except:
        return False


def test_registration_success():
    driver = webdriver.Chrome()
    driver.get(urls.url_register_page)

    try:
        fill_registration_form(driver, data.user_name, data.user_email, data.user_password)

        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *locators.locator_login_user_enter_button
            )
        )

        assert True
    except:
        assert False
    finally:        
        driver.quit()


def test_registration_password_small_failed():
    user_password_wrong = '123'

    driver = webdriver.Chrome()
    driver.get(urls.url_register_page)
    
    try:
        fill_registration_form(driver, data.user_name, data.user_email, user_password_wrong)
        driver.find_element(*locators.locator_wrong_password_text)
    except:
        assert False
    finally:
        driver.quit()
