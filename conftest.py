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
