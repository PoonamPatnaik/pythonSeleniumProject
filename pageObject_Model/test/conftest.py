import os
import pytest
from selenium import webdriver
browser = None



def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture(scope="function")
def launch_brower(request):
    global browser
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_name):
    browser.get_screenshot_as_file(file_name)

