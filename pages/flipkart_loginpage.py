from selenium.webdriver.common.by import By

from base.basedriver import BaseDriver
from pages.homepage import LoginPage


class FkLogin(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    phn_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input"
    pwd_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input"
    login_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button"

    def phn_input(self, ele):
        phn = self.driver.find_element(By.XPATH, self.phn_xpath)
        phn.send_keys(ele)

    def pwd_input(self, ele):
        pwd = self.driver.find_element(By.XPATH, self.pwd_xpath)
        pwd.send_keys(ele)

    def login_button(self):
        return self.driver.find_element(By.XPATH, self.login_xpath)

    @property
    def home(self):
        return LoginPage(self.driver)
