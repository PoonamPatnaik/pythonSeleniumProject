import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Rachel"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alert_txt = alert.text
assert name in alert_txt
alert.accept()

# handling dism