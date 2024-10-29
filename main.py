from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
# Указываем путь к chromedriver.exe
chromedriver_path = "C:\\Users\\zolot\\Desktop\\try py\\chrome\\chromedriver.exe"
url='https://fkr.eiasmo.ru'
# Создаем объект Service и передаем путь к драйверу
service = Service(executable_path=chromedriver_path)
ua = UserAgent()
options= webdriver.ChromeOptions()
options.add_argument(f"user-agent={ua.random}")
options.add_argument("--disable-blink-features=AutomationControlled")
# Инициализируем драйвер Chrome с использованием Service
driver = webdriver.Chrome(service=service, options=options)
try:
    # Переход на страницу с камерами
    driver.get(url=url)
    time.sleep(2)
    login_input = driver.find_element(By.CLASS_NAME, 'form_auth__input')
    login_input.send_keys('isaev_im')
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys('12wq10e@1')
    time.sleep(2)
    login_button=driver.find_element(By.NAME,'execute').click()
    time.sleep(2)
    new_link = driver.find_element(By.XPATH, '//div[text()="Видеонаблюдение"]').click()
    time.sleep(2)
    link_btn = driver.find_element(By.XPATH, '//span[text()="Список камер видеонаблюдения"]').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    link_btn_last = driver.find_element(By.XPATH, '//div[text()="Список"]').click()
    #Пробуем вывести данные
    soup =  BeautifulSoup(driver.page_source, "lxml")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()