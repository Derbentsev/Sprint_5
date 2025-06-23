from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def register_user(driver, user_email, user_password):
    driver.find_element(By.XPATH, 
                        '//label[contains(., "Email")]/following-sibling::input').send_keys(user_email)
    
    driver.find_element(By.XPATH,
                        '//label[contains(., "Пароль")]/following-sibling::input').send_keys(user_password)

    driver.find_element(By.XPATH, '//button[text()="Войти"]').click()

    # Здесь я проверяю, что мы действительно зашли в ЛК
    # Иначе я не нашел каких-то признаков в интерфейсе, что мы зашли в Профиль
    try:
        driver.find_element(By.XPATH, '//p[text()="Личный Кабинет"]').click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//a[text()="Профиль"]')
            )
        )

        return True
    except:
        return False


def test_login_via_enter_account_success(user_email_fx, user_password_fx):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//button[text()="Войти в аккаунт"]')
        )
    ).click()

    try:
        assert register_user(driver, user_email_fx, user_password_fx)
    except:
        assert False
    finally:
        driver.quit()


def test_login_via_personal_account_click_success(user_email_fx, user_password_fx):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//p[text()="Личный Кабинет"]')
        )
    ).click()

    try:
        assert register_user(driver, user_email_fx, user_password_fx)
    except:
        assert False
    finally:
        driver.quit()


def test_login_via_registration_form_success(user_email_fx, user_password_fx):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[text()="Войти"]')
        )
    ).click()

    try:
        assert register_user(driver, user_email_fx, user_password_fx)
    except:
        assert False
    finally:
        driver.quit()


def test_login_via_recover_password_success(user_email_fx, user_password_fx):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[text()="Восстановить пароль"]')
        )
    ).click()

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//a[text()="Войти"]')
        )
    ).click()

    try:
        assert register_user(driver, user_email_fx, user_password_fx)
    except:
        assert False
    finally:
        driver.quit()


def test_logout_via_press_exit_button_success(user_email_fx, user_password_fx):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')

    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//p[text()="Личный Кабинет"]')
        )
    ).click()

    register_user(driver, user_email_fx, user_password_fx)

    try:
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//button[text()="Выход"]')
            )
        ).click()

        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//button[text()="Войти"]')
            )
        )
        
        assert True
    except:
        assert False
    finally:
        driver.quit()
