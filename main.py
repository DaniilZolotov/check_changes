from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
import os
import telebot

# Указываем путь к chromedriver.exe
chromedriver_path = r"C:\Users\zolot\Desktop\try py\chrome\chromedriver.exe"
url = 'https://fkr.eiasmo.ru'

# БОТИК (Telegram Bot)
bot = telebot.TeleBot('7707385206:AAGrRvyCLKS6dGO_u8wyJf63Q8NOVu-0ltk')
TELEGRAM_CHAT_ID = '-4554782359'

# Папка для скриншотов
screenshot_folder = r'C:\Users\zolot\Desktop\try py\screenshot'  # папка скриншотов

def send_screenshot(photo_path, message_text="Скриншот"):
    """Отправляет фото в Telegram чат."""
    with open(photo_path, 'rb') as photo:
        try:
            bot.send_photo(TELEGRAM_CHAT_ID, photo, caption=message_text)
            print('Скриншот отправлен в Telegram.')
        except Exception as e:
            print(f"Ошибка при отправке сообщения в Telegram: {e}")

def main():
    while True:
        try:
            # Настройки для Selenium
            ua = UserAgent()
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-agent={ua.random}")
            options.add_argument("--disable-blink-features=AutomationControlled")
           #headless mode
            options.add_argument("--headless")
            # Создаем объект Service и передаем путь к драйверу
            service = Service(executable_path=chromedriver_path)
            
            # Инициализируем драйвер Chrome с использованием Service
            driver = webdriver.Chrome(service=service, options=options)
            
            # Переход на страницу с камерами
            driver.get(url=url)
            time.sleep(2)
            
            # Авторизация на сайте
            login_input = driver.find_element(By.CLASS_NAME, 'form_auth__input')
            login_input.send_keys('isaev_im')
            password_input = driver.find_element(By.NAME, 'password')
            password_input.send_keys('12wq10e@1')
            time.sleep(2)
            driver.find_element(By.NAME, 'execute').click()
            time.sleep(2)
            
            # Навигация к разделу видеонаблюдения
            driver.find_element(By.XPATH, '//div[text()="Видеонаблюдение"]').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//span[text()="Список камер видеонаблюдения"]').click()
            time.sleep(2)
            
            # Переключение на новое окно
            driver.switch_to.window(driver.window_handles[-1])
            driver.find_element(By.XPATH, '//div[text()="Список"]').click()
            time.sleep(10)

            # Создание скриншота
            driver.maximize_window()
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            screenshot_name = f'screenshot_{timestamp}.png'
            screenshot_path = os.path.join(screenshot_folder, screenshot_name)
            driver.save_screenshot(screenshot_path)
            print(f'Скриншот сохранен: {screenshot_path}')

            # Отправка скриншота в Telegram
            send_screenshot(screenshot_path, message_text=f'Скриншот от {timestamp}')
            
            # Закрываем драйвер перед следующим циклом
            driver.quit()
            
            # Ждем 60 секунд перед следующим скриншотом
            time.sleep(60)

        except Exception as ex:
            print(f"Произошла ошибка: {ex}")
            # Закрываем драйвер в случае ошибки
            driver.quit()
            # Ждем некоторое время перед повторной попыткой
            time.sleep(60)

if __name__ == "__main__":
    main()