import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#Implicitwait
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("br")
time.sleep(2)
filtered_product = driver.find_elements(By.CSS_SELECTOR,".product-action")
print(len(filtered_product))
for product in filtered_product:
    product.click()
driver.find_element(By.XPATH,"//img [@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text() ='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# Explicitwait
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
couponDetails = driver.find_element(By.CLASS_NAME,"promoInfo").text
assert couponDetails == "Code applied ..!"
