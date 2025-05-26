from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time

GECKODRIVER_PATH = r"C:\Users\danich\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe"
BASE_URL = "https://demo.opencart.com/"

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=Service(GECKODRIVER_PATH), options=options)
driver.maximize_window()

try:
    # 1. Клик на продукт и проверка переключения скриншотов
    driver.get(BASE_URL)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".product-thumb h4 a").click()
    time.sleep(2)
    thumbnails = driver.find_elements(By.CSS_SELECTOR, ".image-additional a")
    for thumb in thumbnails:
        thumb.click()
        time.sleep(1)

    # 2. Смена валюты
    driver.get(BASE_URL)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".btn-group .dropdown-toggle").click()
    driver.find_element(By.NAME, "EUR").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".btn-group .dropdown-toggle").click()
    driver.find_element(By.NAME, "USD").click()
    time.sleep(1)

    # 3. Переход в категорию PC и проверка пустой страницы
    driver.get(BASE_URL)
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Desktops").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "PC (0)").click()
    time.sleep(2)
    assert "There are no products to list in this category." in driver.page_source

    # 4. Регистрация пользователя
    driver.find_element(By.CSS_SELECTOR, ".dropdown .dropdown-toggle").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-firstname").send_keys("Test")
    driver.find_element(By.ID, "input-lastname").send_keys("User")
    driver.find_element(By.ID, "input-email").send_keys(f"testuser{int(time.time())}@example.com")
    driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    driver.find_element(By.ID, "input-password").send_keys("Test1234")
    driver.find_element(By.ID, "input-confirm").send_keys("Test1234")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
    time.sleep(3)

    # 5. Поиск товара
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("MacBook")
    driver.find_element(By.CSS_SELECTOR, "#search button").click()
    time.sleep(2)

finally:
    driver.quit()
