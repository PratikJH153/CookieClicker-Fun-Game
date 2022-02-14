from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Downloads\SETUPS\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# articles_count.click()

all_portals = driver.find_element(By.LINK_TEXT, 'All portals')
# all_portals.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# search_button = driver.find_element(By.ID, 'searchButton')
# search_button.click()

# driver.close()
# driver.quit()
