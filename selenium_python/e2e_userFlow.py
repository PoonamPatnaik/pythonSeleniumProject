import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

expected_Productname = "iphone X"
driver.find_element(By.LINK_TEXT,"Shop").click()
Products_cards = driver.find_elements(By.XPATH,"//app-card-list/ app-card")
for card in Products_cards:
    actual_product_name = card.find_element(By.XPATH,"//app-card-list/ app-card/div/div/h4 [@class = 'card-title']").text
    print(actual_product_name)
    if actual_product_name == expected_Productname:
        print("Navigated to expected product card to perform click")
        # product_price = driver.find_element(By.XPATH,"//app-card-list/ app-card/div/div/h5").text
        driver.find_element(By.XPATH,"//app-card-list/ app-card/div/div [2]/button").click()
        driver.find_element(By.XPATH,"//a [@class = 'nav-link btn btn-primary']").click()
        time.sleep(3)
        checkOut_Product = driver.find_element(By.XPATH,"//tr[1]/td/div/div/h4").text
        assert checkOut_Product == expected_Productname
        print("Assertion success")
        break
# Click on checkout
print("Navigated to Checkout page")
driver.find_element(By.XPATH,"//tbody/tr[3]/td[5]").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver, 8)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "suggestions")))
print("Dropdown is loaded")
drop_down_elements = driver.find_elements(By.CSS_SELECTOR,".suggestions ul")
exepected_dd = 'India'
for element in drop_down_elements:
    if element.text == exepected_dd:
       driver.find_element(By.CSS_SELECTOR,".suggestions ul li a").click()
       time.sleep(3)
       print("Able select value from Dynamic drop down")
       selected_country = driver.find_element(By.ID,"country").get_attribute("value")
       print(selected_country)
       assert selected_country == exepected_dd
       break
