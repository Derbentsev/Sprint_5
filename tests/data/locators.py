from selenium.webdriver.common.by import By


def locator_login_user_name():
    return (By.XPATH, '//label[contains(., "Имя")]/following-sibling::input')


def locator_login_user_email():
    return (By.XPATH, '//label[contains(., "Email")]/following-sibling::input')


def locator_login_user_password():
    return (By.XPATH, '//label[contains(., "Пароль")]/following-sibling::input')


def locator_login_user_enter_button():
    return (By.XPATH, '//button[text()="Войти"]')


def locator_personal_account_button():
    return (By.XPATH, '//p[text()="Личный Кабинет"]')


def locator_personal_profile_text():
    return (By.XPATH, '//a[text()="Профиль"]')


def locator_login_user_enter_account_button():
    return (By.XPATH, '//button[text()="Войти в аккаунт"]')


def locator_recover_password_link():
    return (By.XPATH, '//a[text()="Восстановить пароль"]')


def locator_exit_account_button():
    return (By.XPATH, '//button[text()="Выход"]')


def locator_create_burger_text():
    return (By.XPATH, '//h1[text()="Соберите бургер"]')


def locator_logo_text():
    return (By.CSS_SELECTOR, 'div[class*="AppHeader_header__logo__"]')


def locator_constructor_text():
    return (By.XPATH, '//p[text()="Конструктор"]')


def locator_register_button():
    return (By.XPATH, '//button[text()="Зарегистрироваться"]')


def locator_wrong_password_text():
    return (By.XPATH, '//p[text()="Некорректный пароль"]')
