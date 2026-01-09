import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
static_dropdown = Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
static_dropdown.select_by_visible_text("Male")
time.sleep(5)

driver.find_element(By.ID,"email").send_keys("Ross")



# https://rahulshettyacademy.com/angularpractice/
#https://rahulshettyacademy.com/AutomationPractice/