from selenium.webdriver.common.by import By
import time


# авторизация
def auth1(browser):
    email = browser.find_element(By.NAME, 'login')
    password = browser.find_element(By.NAME, 'password')
    email.send_keys('admin')
    password.send_keys('admin')
    browser.find_element(By.CLASS_NAME, 'login__button').click()

# Тест входные_данные_вариант1
def input_data_option1(browser, by, value):
    browser.find_element(by, value).click()
    browser.find_element(By.NAME, 'InvestigationNumber').send_keys('входные_данные_вариант1')
    inputs_wrapper = browser.find_elements(By.CSS_SELECTOR,'.tasks-modal__entry-parameter')
    inputs = []
    dict_input_values = {"Поисковый запрос": "Пустышкин Василий Петрович", 'Электронная почта': 'pustishkinv@gmail.com',
                         'Номер телефона': '9697073549',
                         'Имя пользователя в сети': 'pvp01021975', 'Год рождения человека': '1975',
                         'Имя Фамилия': 'Василий Пустышкин',
                         'Город проживания человека': 'Санкт-Петербург', 'Страна проживания человека': 'Россия',
                         'Фамилия Имя Отчество': 'Пустышкин Василий Петрович'}
    for i in inputs_wrapper:
        inputs.append(i.find_element_by_css_selector('input'))
    for k,v in dict_input_values.items():
        for single_input in inputs:
            if k == single_input.get_attribute('placeholder'):
                single_input.send_keys(v)
    browser.find_element(By.CLASS_NAME, 'avtotest').click()

# Тест входные_данные_вариант0
def input_data_option0(browser, by, value):
    browser.find_element(by, value).click()
    browser.find_element(By.NAME, 'InvestigationNumber').send_keys('входные_данные_вариант0')
    inputs_wrapper = browser.find_elements(By.CSS_SELECTOR, '.tasks-modal__entry-parameter')
    inputs = []
    dict_input_values = {'Поисковый запрос': 'Пустышкин Василий Петрович', 'Имя Фамилия': 'Василий Пустышкин',
                         'Страна проживания человека': 'Россия', 'Имя пользователя в сети': 'pvp01021975',
                         'Город проживания человека': 'Санкт-Петербург'}
    for i in inputs_wrapper:
        inputs.append(i.find_element(By.CSS_SELECTOR, 'input'))
    for k, v in dict_input_values.items():
        for single_input in inputs:
            if k == single_input.get_attribute('placeholder'):
                single_input.send_keys(v)
    browser.find_element(By.CLASS_NAME, 'avtotest').click()

def input_data_geo(browser, by, value):
    browser.find_element(by, value).click()
    browser.find_element(By.NAME, 'InvestigationNumber').send_keys('задача_геопоиск_вариант1')
    inputs_wrapper = browser.find_elements(By.CSS_SELECTOR, '.tasks-modal__entry-parameter')
    inputs = []
    for i in inputs_wrapper:
        inputs.append(i.find_element(By.CSS_SELECTOR, 'input'))
    for single_input in inputs:
        if single_input.get_attribute('placeholder') == 'Точный адрес':
            single_input.send_keys('наб. Обводного канала, 211-213, Санкт-Петербург, Россия')
    browser.find_element(By.CLASS_NAME, 'avtotest').click()




