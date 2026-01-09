import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("ind")
# time.sleep(2)
# #driver.find_element(By.CSS_SELECTOR,"li [ class='ui-corner-all' ] a").click()
# dynamic_dropdown = driver.find_elements(By.XPATH,"//*[@id='ui-id-1']/li")
# for element in dynamic_dropdown:
#     if element.text == "India":
#         print(element.text)
#         element.click()
#         time.sleep(3)
#         break
# selected_value = driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute("value")
# assert selected_value == "India"
# time.sleep(5)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Handling checkbox
options = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(options))

for option in options:
    print(option.get_attribute("value"))
    if option.get_attribute("value") == "option2":
        option.click()
        print("clicked")
        assert option.is_selected()
        break

time.sleep(2)

# handling Radio button //input[@name='radioButton']
radiobuttons = driver.find_elements(By.XPATH,"//input[@name='radioButton']")
print(len(radiobuttons))
# method to select by value
# for button in radiobuttons:
#     print(button.get_attribute("value"))
#     if button.get_attribute("value") == "radio2":
#         button.click()
#         print("clicked")
#         assert button.is_selected()
#         break
# time.sleep(2)
# method to select by index
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


#is_displayed validation returns boolen
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()




#dynamic_list = driver.find_elements(By.CSS_SELECTOR,"#autosuggest")


