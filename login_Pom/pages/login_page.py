from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    password = (By.NAME, "password")
    checkbox = (By.ID, "terms")
    signin_btn = (By.CSS_SELECTOR, "#signInBtn")

    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_terms(self):
        self.driver.find_element(*self.checkbox).click()

    def click_signin(self):
        self.driver.find_element(*self.signin_btn).click()
