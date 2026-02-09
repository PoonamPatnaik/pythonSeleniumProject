import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pageObject_Model.utils.browser_utils import BrowserUtils


class ShoppingCartPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shopLink = (By.LINK_TEXT, "Shop")
        self.totalproductList= (By.XPATH, "//app-card-list/ app-card")
        self.actualProductname = (By.XPATH,"//app-card-list/ app-card/div/div/h4 [@class = 'card-title']")
        self.addButton = (By.XPATH, "//app-card-list/ app-card/div/div [2]/button")
        self.checkoutLink = (By.XPATH, "//a [@class = 'nav-link btn btn-primary']")
        self.checkedoutProductName = (By.XPATH, "//tr[1]/td/div/div/h4")

    def addProductToShoppingCartPage(self,productname):
        self.driver.find_element(*self.shopLink).click()
        Products_cards = self.driver.find_elements(*self.totalproductList)
        for card in Products_cards:
            actual_product_name = card.find_element(*self.actualProductname).text
            print(actual_product_name)
            if actual_product_name == productname:
                print("Running using Pytest: Navigated to expected product card to perform click")
                # product_price = driver.find_element(By.XPATH,"//app-card-list/ app-card/div/div/h5").text
                self.driver.find_element(*self.addButton).click()
                self.driver.find_element(*self.checkoutLink).click()
                time.sleep(3)
                checkOut_Product = self.driver.find_element(*self.checkedoutProductName).text
                assert checkOut_Product == productname
                print("Assertion success")
                break
            #clicking on Checkout button
        self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]").click()

        # Click on checkout
    def navigateToCheckoutCartPage(self):
        print("Running using Pytest: Navigated to Checkout page")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 8)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "suggestions")))
        print("Running using Pytest: :Dropdown is loaded")
        drop_down_elements = self.driver.find_elements(By.CSS_SELECTOR, ".suggestions ul")
        exepected_dd = 'India'
        for element in drop_down_elements:
            if element.text == exepected_dd:
                self.driver.find_element(By.CSS_SELECTOR, ".suggestions ul li a").click()
                time.sleep(3)
                print("Able select value from Dynamic drop down")
                selected_country = self.driver.find_element(By.ID, "country").get_attribute("value")
                print(selected_country)
                assert selected_country == exepected_dd
                break
        self.driver.find_element(By.XPATH, "//label [@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input [@type='submit']").click()
        expected_message = "Success!"
        actual_message = self.driver.find_element(By.XPATH, "//div/strong").text
        assert expected_message == actual_message