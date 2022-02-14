from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Downloads\SETUPS\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, 'fName')
first_name_input.send_keys("Pratik")

first_name_input = driver.find_element(By.NAME, 'lName')
first_name_input.send_keys("JH")

first_name_input = driver.find_element(By.NAME, 'email')
first_name_input.send_keys("pratik@gmail.com")

sign_up_button = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up_button.click()
