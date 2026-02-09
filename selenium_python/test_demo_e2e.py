import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import sys

sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )
from pageObject_Model.pages.loginPage import LoginPage




def test_demo(launch_brower):
    # driver = webdriver.Chrome()
    driver = launch_brower

    loginPage = LoginPage(driver)
    loginPage.login()

    # #Logging & sending value
    # driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    # driver.find_element(By.NAME, "password").send_keys("Learning@830$3mK2")
    # # Click on checkbox
    # driver.find_element(By.XPATH, "//input[@id='terms']").click()
    # # click on Radio button
    # # select value from static dropdown
    # static_dd = Select(driver.find_element(By.XPATH, "//select[@class ='form-control']"))
    # static_dd.select_by_value("teach")
    # # Click on button
    # driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

    # Redirected to Product Listing Pag
    print("Running using Pytest: Navigated to Product listing page")
    expected_Productname = "iphone X"
    driver.find_element(By.LINK_TEXT,"Shop").click()
    Products_cards = driver.find_elements(By.XPATH,"//app-card-list/ app-card")
    for card in Products_cards:
        actual_product_name = card.find_element(By.XPATH,"//app-card-list/ app-card/div/div/h4 [@class = 'card-title']").text
        print(actual_product_name)
        if actual_product_name == expected_Productname:
            print("Running using Pytest: Navigated to expected product card to perform click")
            # product_price = driver.find_element(By.XPATH,"//app-card-list/ app-card/div/div/h5").text
            driver.find_element(By.XPATH,"//app-card-list/ app-card/div/div [2]/button").click()
            driver.find_element(By.XPATH,"//a [@class = 'nav-link btn btn-primary']").click()
            time.sleep(3)
            checkOut_Product = driver.find_element(By.XPATH,"//tr[1]/td/div/div/h4").text
            assert checkOut_Product == expected_Productname
            print("Assertion success")
            break
    # Click on checkout
    print("Running using Pytest: Navigated to Checkout page")
    driver.find_element(By.XPATH,"//tbody/tr[3]/td[5]").click()
    driver.find_element(By.ID,"country").send_keys("ind")
    wait = WebDriverWait(driver, 8)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "suggestions")))
    print("Running using Pytest: :Dropdown is loaded")
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
    driver.find_element(By.XPATH,"//label [@for='checkbox2']").click()
    driver.find_element(By.XPATH,"//input [@type='submit']").click()
    expected_message = "Success!"
    actual_message = driver.find_element(By.XPATH,"//div/strong").text
    assert expected_message == actual_message
    print("Running using Pytest: :Assertion success Post transaction Completion")