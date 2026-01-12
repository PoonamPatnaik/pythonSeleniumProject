import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("br")
time.sleep(2)
Expected_filtered_item = ["Brocolli - 1 Kg","Brinjal - 1 Kg"]
Actual_item_list = driver.find_elements(By.XPATH,"//div[@class='product']")
actual_item_name = []
for item in Actual_item_list:
    # Chaining of Xpath
    value = item.find_element(By.XPATH,"h4").text
    actual_item_name.append(value)
    item.find_element(By.XPATH, "//div[@class='product-action']/button").click()
assert actual_item_name == Expected_filtered_item
print("Assertion Completed")





# adding item , applying Promo and checkout

# filtered_product = driver.find_elements(By.CSS_SELECTOR,".product-action")
# print(len(filtered_product))
# for product in filtered_product:
#     product.click()
# driver.find_element(By.XPATH,"//img [@alt='Cart']").click()
# driver.find_element(By.XPATH,"//button[text() ='PROCEED TO CHECKOUT']").click()
# driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# time.sleep(7)
# couponDetails = driver.find_element(By.CLASS_NAME,"promoInfo").text
# assert couponDetails == "Code applied ..!"
# # total_amount = driver.find_element(By.CLASS_NAME,"totAmt").text     //getting value from element path
# total_amount = 0.0
# amount = driver.find_elements(By.XPATH,"//table [@class='cartTable']/tbody/tr/td [5]")
# for value in amount:
#     total_amount = total_amount + float(value.text)
#
# discounted_amount = float(driver.find_element(By.CLASS_NAME,"discountAmt").text)
# assert total_amount >  discounted_amount
# print("Code has been applied")
#
#
#
