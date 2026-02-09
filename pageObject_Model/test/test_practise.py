import time
from selenium.webdriver.common.by import By

def test_practise(launch_brower):
    print("Running 2nd test cases in POM")
    driver = launch_brower
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    name = "Rachel"
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Ross")
    driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert_txt = alert.text
    assert name in alert_txt
    alert.accept()