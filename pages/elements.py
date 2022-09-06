from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement as seleniumWebElement
import time


class WebElement:
    driver = None

    def __init__(self, driver: webdriver,  **kwargs):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)
        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self) -> seleniumWebElement:
        element = None
        try:
            element = self._wait.until(ec.presence_of_element_located(self._locator))
        except Exception as e:
            print(e)

        return element

    def is_visible(self) -> bool:
        element = self.find()
        if element:
            return element.is_displayed()

        return False

    def send_keys(self, keys: str, wait: int = 2) -> None:
        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def press_enter(self) -> None:
        element = self.find()
        element.send_keys(Keys.ENTER)

    def get_href(self) -> str:
        element = self.find()
        return element.get_attribute("href")


class WebElements(WebElement):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)

    def find(self):
        """ Find elements on the page. """

        elements = []

        try:
            elements = self._wait.until(
                ec.presence_of_all_elements_located(self._locator)
            )
        except Exception as e:
            print('Elements not found on the page!')
            print(e)

        return elements

    def get_attributes(self, attribute: str):
        results = []
        elements = self.find()

        for element in elements:
            results.append(element.get_attribute(attribute))

        return results
