import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from test_auth import auth1, input_data_option0, input_data_option1, input_data_geo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_task0():
    with Chrome() as browser:
        browser.get('there is url')
        browser.maximize_window()
        auth1(browser)
        time.sleep(2)
        by, value = By.CLASS_NAME, '-plus'
        input_data_option0(browser, by, value)
        name_task = 'toast1'
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((by, name_task)))
        time.sleep(2)
        assert browser.find_element(by, name_task).text == 'Задача успешно создана', \
            'Создание задачи по входные_данные_вариант0 выполнено с ошибкой'
        print(browser.find_element(by, name_task).text)


def test_task1():
    with Chrome() as browser:
        browser.get('there is url')
        browser.maximize_window()
        auth1(browser)
        time.sleep(2)
        by, value = By.CLASS_NAME, '-plus'
        input_data_option1(browser, by, value)
        name_task = 'toast1'
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((by, name_task)))
        time.sleep(2)
        assert browser.find_element(by, name_task).text == 'Задача успешно создана', \
            'Создание задачи по входные_данные_вариант1 выполнено с ошибкой'
        print(browser.find_element(by, name_task).text)

def test_geo():
    with Chrome() as browser:
        browser.get('there is url')
        browser.maximize_window()
        auth1(browser)
        time.sleep(2)
        by, value = By.CLASS_NAME, '-plus'
        input_data_geo(browser, by, value)
        name_task = 'toast1'
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((by, name_task)))
        time.sleep(2)
        assert browser.find_element(by, name_task).text == 'Задача успешно создана', \
            'Создание задачи по задача_геопоиск_вариант1 выполнено с ошибкой'
        print(browser.find_element(by, name_task).text)
