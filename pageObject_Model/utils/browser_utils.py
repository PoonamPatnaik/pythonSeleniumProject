class BrowserUtils:
    def __init__(self,driver):
        self.driver = driver
    def get_Title(self):
        return self.driver.title