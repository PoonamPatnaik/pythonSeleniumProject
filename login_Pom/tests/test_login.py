from login_Pom.pages.login_page import LoginPage
from login_Pom.utils.config_reader import get_test_data

def test_login(browser):
    data = get_test_data()
    print(data)
    login_data = data["login"]
    print(login_data)

    browser.get("https://rahulshettyacademy.com/loginpagePractise/")
    login = LoginPage(browser)

    login.enter_username(login_data["username"])
    login.enter_password(login_data["password"])
    login.click_terms()
    login.click_signin()
