from tests.data import data
from tests.data import locators
from tests.data import urls

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_success(chrome_driver, fill_registration_form_factory):
    driver = chrome_driver
    driver.get(urls.url_register_page)

    try:
        fill_registration_form_factory(driver, data.user_name, data.user_email, data.user_password)

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


def test_registration_password_small_failed(chrome_driver, fill_registration_form_factory):
    user_password_wrong = '123'

    driver = chrome_driver
    driver.get(urls.url_register_page)
    
    try:
        fill_registration_form_factory(driver, data.user_name, data.user_email, user_password_wrong)
        driver.find_element(*locators.locator_wrong_password_text)
    except:
        assert False
    finally:
        driver.quit()
