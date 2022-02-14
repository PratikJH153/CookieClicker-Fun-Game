from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time

chrome_driver_path = "D:\Downloads\SETUPS\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.ID, "bigCookie")
timeout = time.time() + 5
times = 0

while True:
    cookie.click()
    test = 0
    if test == 5 or time.time() > timeout:
        powerup = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
        powerup[-1].click()
        test = 0
        timeout = time.time() + 5

    test -= 1

driver.close()
driver.quit()
