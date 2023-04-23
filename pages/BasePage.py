import conftest


class BasePage:

    def __init__(self):
        self.driver = conftest.driver

    def findElement(self, locator):
        return self.driver.find_element(*locator)

    def fillField(self, locator, text):
        self.findElement(locator).send_keys(text)

    def click(self, locator):
        self.findElement(locator).click()

    def checkIfExists(self, locator):
        assert self.findElement(locator).is_displayed(), f"The element '{locator}' is not present in this page."

    def isEnableCheck(self, locator):
        assert self.findElement(locator).is_enabled(), f"The element '{locator}' is not enable in this page."
