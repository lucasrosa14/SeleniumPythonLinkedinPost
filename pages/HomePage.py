from selenium.webdriver.common.by import By

import conftest
from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.startPost = (By.XPATH, "//*[text()='Começar publicação']")
        self.writeText = (By.XPATH, "//*[@data-placeholder='No que você está pensando?']")
        self.postButton = (By.XPATH, "//*[text()='Publicar']")
        self.visualizePost = (By.XPATH, "//*[text()='Visualize a publicação']")

    def checkLoginSuccess(self):
        self.checkIfExists(self.startPost)

    def writePost(self, text):
        self.click(self.startPost)
        self.fillField(self.writeText, text)

    def sharePost(self):
        self.isEnableCheck(self.postButton)
        self.click(self.postButton)

    def checkPosted(self):
        assert self.checkIfExists(self.visualizePost)
        self.click(self.visualizePost)
