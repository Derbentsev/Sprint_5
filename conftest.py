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
def login_user_method_fx():
    driver = webdriver.Chrome()
    driver.get(urls.url_login_account)

    driver.find_element(*locators.locator_login_user_email).send_keys(data.user_email)
    
    driver.find_element(*locators.locator_login_user_password).send_keys(data.user_password)

    driver.find_element(*locators.locator_login_user_enter_button).click()

    driver.find_element(*locators.locator_personal_account_button).click()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            *locators.locator_personal_profile_text
        )
    )

    driver.find_element(*locators.locator_logo_text).click()

    yield driver
    driver.quit()


@pytest.fixture
def register_factory():
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
        
    return register_user


@pytest.fixture
def enter_section_factory():
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
        
    return enter_section


#Заполняем форму регистрации и логинимся
def fill_registration_form_factory():
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

    return fill_registration_form
