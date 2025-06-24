import random


def user_name():
    return 'Сергей'


def user_email():
    return 'Sergey_D_23_000@bts.ru'


def user_email_random():
    return f'Sergey_D_23_{random.randint(0, 999):03d}@bts.ru'


def user_password():
    return '123987'
