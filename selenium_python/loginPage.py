import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# sending value
driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
driver.find_element(By.NAME, "password").send_keys("Learning@830$3mK2")
# Click on checkbox
driver.find_element(By.XPATH, "//input[@id='terms']").click()
# click on Radio button
# select value from static dropdown
static_dd = Select(driver.find_element(By.XPATH, "//select[@class ='form-control']"))
static_dd.select_by_value("teach")

# Click on button
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()

time.sleep(4)

