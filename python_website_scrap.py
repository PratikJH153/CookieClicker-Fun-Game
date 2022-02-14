from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Downloads\SETUPS\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.python.org/")

events = {}

time_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu time')
name_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')

for index, time_event in enumerate(time_events):
    events[time_event.text] = name_events[index].text

print(events)

driver.close()
driver.quit()
