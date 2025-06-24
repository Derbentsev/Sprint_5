import pytest
from tests.data import data
from tests.data import locators
from tests.data import urls

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login_user_method_fx(chrome_driver):
    chrome_driver.get(urls.url_login_account)

    chrome_driver.find_element(*locators.locator_login_user_email).send_keys(data.user_email)    
    chrome_driver.find_element(*locators.locator_login_user_password).send_keys(data.user_password)
    chrome_driver.find_element(*locators.locator_login_user_enter_button).click()
    chrome_driver.find_element(*locators.locator_personal_account_button).click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.visibility_of_element_located(
            *locators.locator_personal_profile_text
        )
    )

    chrome_driver.find_element(*locators.locator_logo_text).click()
    yield chrome_driver


@pytest.fixture
def register_user_factory():
    def register_user(driver, user_email, user_password):
        driver.find_element(*locators.locator_login_user_email).send_keys(user_email)        
        driver.find_element(*locators.locator_login_user_password).send_keys(user_password)
        driver.find_element(*locators.locator_login_user_enter_button).click()
        driver.find_element(*locators.locator_personal_account_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                *By.XPATH, locators.locator_personal_profile_text
            )
        )
        
    return register_user


@pytest.fixture
def enter_section_factory():
    def enter_section(driver, section_name):
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
        
    return enter_section


#Заполняем форму регистрации и логинимся
def fill_registration_form_factory():
    def fill_registration_form(driver, user_name, user_email, user_password):
        print(f'{user_email} : {user_password}')

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                *locators.locator_login_user_name)
        ).send_keys(user_name)
        
        driver.find_element(*locators.locator_login_user_email).send_keys(user_email)            
        driver.find_element(*locators.locator_login_user_password).send_keys(user_password)
        driver.find_element(*locators.locator_register_button).click()

    return fill_registration_form
