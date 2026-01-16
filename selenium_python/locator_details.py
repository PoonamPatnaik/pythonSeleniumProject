from selenium_python.test_locators import launch_browser, test_mouseOver

driver = launch_browser()
mouse_over_ele = "button#mousehover"
assert  test_mouseOver(driver, mouse_over_ele)
# selects the 1st element of the list
click_on_mouseOver_ele = "div.mouse-hover > div > a:first-of-type"
assert  test_mouseOver(driver, click_on_mouseOver_ele)
# selects the 1st element of the list
click_on_mouseOver_ele2 = "div.mouse-hover > div > a:nth-of-type(2)"
assert  test_mouseOver(driver, click_on_mouseOver_ele2)




