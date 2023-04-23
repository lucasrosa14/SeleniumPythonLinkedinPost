from selenium.webdriver.common.by import By

import conftest
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.userNameField = (By.ID, "username")
        self.passwordField = (By.ID, "password")
        self.loginButton = (By.XPATH, "//*[@type='submit']")

    def doLogin(self, username, password):
        self.fillField(self.userNameField, username)
        self.fillField(self.passwordField, password)
        self.click(self.loginButton)
