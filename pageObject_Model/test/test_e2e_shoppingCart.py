import json
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import sys

sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )
from pageObject_Model.pages.loginPage import LoginPage
from pageObject_Model.pages.shoppingCartPage import ShoppingCartPage

test_data_path = '../data/login_checkout.json'
with open( test_data_path ) as f:
    test_data = json.load( f )
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize( "test_list_item", test_list )
def test_demo(launch_brower,test_list_item):
    # driver = webdriver.Chrome()
    print("Running Shopping Cart test cases in POM")

    driver = launch_brower

    # User logins with valida data
    loginPage = LoginPage(driver)
    # Fetch dats from data file
    username =test_list_item["username"]
    password =test_list_item["password"]
    loginPage.login(username,password)
    print(loginPage.get_Title())

    shoppingPage = ShoppingCartPage(driver)
    print(shoppingPage.get_Title())
    product =test_list_item["productName"]
    shoppingPage.addProductToShoppingCartPage(product)
    shoppingPage.navigateToCheckoutCartPage()





    # Redirected to Product Listing Pag
    # print("Running using Pytest: Navigated to Product listing page")
    # expected_Productname = test_list_item["productName"]
    # driver.find_element(By.LINK_TEXT,"Shop").click()
    # Products_cards = driver.find_elements(By.XPATH,"//app-card-list/ app-card")
    # # adding given Product
    # for card in Products_cards:
    #     actual_product_name = card.find_element(By.XPATH,"//app-card-list/ app-card/div/div/h4 [@class = 'card-title']").text
    #     print(actual_product_name)
    #     if actual_product_name == expected_Productname:
    #         print("Running using Pytest: Navigated to expected product card to perform click")
    #         # product_price = driver.find_element(By.XPATH,"//app-card-list/ app-card/div/div/h5").text
    #         driver.find_element(By.XPATH,"//app-card-list/ app-card/div/div [2]/button").click()
    #         driver.find_element(By.XPATH,"//a [@class = 'nav-link btn btn-primary']").click()
    #         time.sleep(3)
    #         checkOut_Product = driver.find_element(By.XPATH,"//tr[1]/td/div/div/h4").text
    #         assert checkOut_Product == expected_Productname
    #         print("Assertion success")
    #         break
    # # Click on checkout
    # print("Running using Pytest: Navigated to Checkout page")
    # driver.find_element(By.XPATH,"//tbody/tr[3]/td[5]").click()
    # driver.find_element(By.ID,"country").send_keys("ind")
    # wait = WebDriverWait(driver, 8)
    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "suggestions")))
    # print("Running using Pytest: :Dropdown is loaded")
    # drop_down_elements = driver.find_elements(By.CSS_SELECTOR,".suggestions ul")
    # exepected_dd = 'India'
    # for element in drop_down_elements:
    #     if element.text == exepected_dd:
    #        driver.find_element(By.CSS_SELECTOR,".suggestions ul li a").click()
    #        time.sleep(3)
    #        print("Able select value from Dynamic drop down")
    #        selected_country = driver.find_element(By.ID,"country").get_attribute("value")
    #        print(selected_country)
    #        assert selected_country == exepected_dd
    #        break
    # driver.find_element(By.XPATH,"//label [@for='checkbox2']").click()
    # driver.find_element(By.XPATH,"//input [@type='submit']").click()
    # expected_message = "Success!"
    # actual_message = driver.find_element(By.XPATH,"//div/strong").text
    # assert expected_message == actual_message
    # print("Running using Pytest: :Assertion success Post transaction Completion")