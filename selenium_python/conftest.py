import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser", action="store")
@pytest.fixture
def launch_brower(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        browser = webdriver.Chrome()
    browser.get("https://rahulshettyacademy.com/loginpagePractise/")
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()