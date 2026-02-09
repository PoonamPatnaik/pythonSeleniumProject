from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObject_Model.utils.browser_utils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_loc = (By.ID, "username")
        self.password_loc= (By.NAME, "password")
        self.checkbox_loc= (By.XPATH, "//input[@id='terms']")
        self.staticdd_loc = (By.XPATH, "//select[@class ='form-control']")
        self.login_button_loc = (By.CSS_SELECTOR, "#signInBtn")

        # Logging & sending value
    def login(self,username,password):
        self.driver.find_element(*self.username_loc).send_keys(username)
        self.driver.find_element(*self.password_loc).send_keys(password)
        # Click on checkbox
        self.driver.find_element(*self.checkbox_loc).click()
        # click on Radio button
        # select value from static dropdown
        static_dd = Select(self.driver.find_element(*self.staticdd_loc))
        static_dd.select_by_value("teach")
        # Click on button
        self.driver.find_element(*self.login_button_loc).click()
