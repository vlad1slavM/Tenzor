from pages.elements import WebElement, WebElements
from pages.base import WebBase


class MainPage(WebBase):
    def __init__(self, driver, url="https://yandex.ru"):
        super().__init__(driver, url)
        self.search_field = WebElement(self.driver,  class_name="input__control")
        self.links_list = WebElements(self.driver, class_name="Link")
