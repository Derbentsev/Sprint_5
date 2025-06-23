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
                (By.XPATH, '//label[contains(.,  "Имя")]/following-sibling::input'))
        ).send_keys(user_name)
        
        driver.find_element(By.XPATH, 
                            '//label[contains(., "Email")]/following-sibling::input').send_keys(user_email)
        
        driver.find_element(By.XPATH,
                            '//label[contains(., "Пароль")]/following-sibling::input').send_keys(user_password)

        driver.find_element(By.XPATH,
                            '//button[text()="Зарегистрироваться"]').click()
        
        return True
    except:
        return False


def test_registration_success(user_name_fx, user_email_random_fx, user_password_fx):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')

    try:
        fill_registration_form(driver, user_name_fx, user_email_random_fx, user_password_fx)

        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//button[text()="Войти"]')
            )
        )

        assert True
    except:
        assert False
    finally:        
        driver.quit()


def test_registration_password_small_failed(user_name_fx, user_email_fx):
    user_password_wrong = '123'

    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    
    try:
        fill_registration_form(driver, user_name_fx, user_email_fx, user_password_wrong)
        driver.find_element(By.XPATH, '//p[text()="Некорректный пароль"]')
    except:
        assert False
    finally:
        driver.quit()
