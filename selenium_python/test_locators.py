import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def launch_browser():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    return driver

def test_mouseOver(driver, locator):
    driver.implicitly_wait(5)
    action = ActionChains(driver)
    print("action var created")
    element = driver.find_element(By.CSS_SELECTOR, locator)
    name = element.text
    print("Got the mouseOver element as",name)
    action.move_to_element(element).perform()
    print("Moved to the element")

    return 1


