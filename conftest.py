import pytest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def user_name_fx():
    return 'Сергей'


@pytest.fixture(scope='module')
def user_email_fx():
    return 'Sergey_D_23_000@bts.ru'


@pytest.fixture
def user_email_random_fx():
    return f'Sergey_D_23_{random.randint(0, 999):03d}@bts.ru'


@pytest.fixture(scope='module')
def user_password_fx():
    return '123987'

@pytest.fixture(scope='module')
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def login_user_method_fx(user_email_fx, user_password_fx):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/account')

    driver.find_element(By.XPATH, 
                        '//label[contains(., "Email")]/following-sibling::input').send_keys(user_email_fx)
    
    driver.find_element(By.XPATH,
                        '//label[contains(., "Пароль")]/following-sibling::input').send_keys(user_password_fx)

    driver.find_element(By.XPATH, '//button[text()="Войти"]').click()

    driver.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, '//a[text()="Профиль"]')
        )
    )

    driver.find_element(By.CSS_SELECTOR, '[class*="AppHeader_header__logo__"]').click()

    yield driver

    driver.quit()
