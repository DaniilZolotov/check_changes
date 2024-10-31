from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import os
import telebot
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
screenshot_folder = r'C:\Users\zolot\Desktop\try py\screenshot' #папкаскриншотов

#БОТИК
bot = telebot.TeleBot('7707385206:AAGrRvyCLKS6dGO_u8wyJf63Q8NOVu-0ltk')
TELEGRAM_CHAT_ID= '-4554782359'    
def send_screenshot(photo_path, message_text="Скриншот"):
    """Отправляет фото в Telegram чат."""
    with open(photo_path, 'rb') as photo:
        try:
            bot.send_photo(TELEGRAM_CHAT_ID, photo, caption=message_text)
            print('Скриншот отправлен в Telegram.')
        except Exception as e:
            print(f"Ошибка при отправке сообщения в Telegram: {e}")

def main():
    # Настройка опций для браузера
    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={ua.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless") 



try:
    while True:
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
        # soup =  BeautifulSoup(driver.page_source, "lxml")
        # all_elemets = soup.find_all("div")
        # elements = driver.find_elements(By.CSS_SELECTOR, "background-color")
        # for element in elements:
        #     print(element)
        time.sleep(10)
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        screenshot_name = f'screenshot_{timestamp}.png'
        screenshot_path = os.path.join(screenshot_folder, screenshot_name)
        driver.save_screenshot(screenshot_path)
        print(f'Скриншот сохранен: {screenshot_path}')
    #Пока будем делать скриншоты, а не вывод кода
            # Ждем 30 минут перед следующим скриншотом
        send_screenshot(screenshot_path, message_text=f'Скриншот от {timestamp}')

        time.sleep(20)  # 1800 секунд = 30 минут    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()