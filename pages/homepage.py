from selenium.webdriver.common.by import By

from base.basedriver import BaseDriver


class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    username_xpath = "/html/body/div/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div"

    def username(self):
        return self.driver.find_element(By.XPATH, self.username_xpath)
