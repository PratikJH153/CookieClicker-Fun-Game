from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Downloads\SETUPS\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[1]/td[2]/span[1]')

# print(price.text)

search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
print(link.text)

# CLOSES JUST THE TAB
driver.close()

# CLOSES THE WHOLE DRIVER/ BROWSER
driver.quit()
