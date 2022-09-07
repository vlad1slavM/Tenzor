from pages.elements import WebElement, WebElements
from pages.base import WebBase


class MainPage(WebBase):
    def __init__(self, driver, url="https://yandex.ru"):
        super().__init__(driver, url)
        self.search_field = WebElement(self.driver, class_name="input__control")
        self.links_list = WebElements(self.driver, class_name="Link")
        self.link_images = WebElement(self.driver,
                                      xpath="/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a")


class ImagesPage(WebBase):
    def __init__(self, driver, url="https://yandex.ru/images/"):
        super().__init__(driver, url)
        self.first_categories = WebElement(self.driver,
                                           xpath="//*[@id=\"PopularRequestList-OCNpd-N\"]/div/div[1]/a/div[1]")
