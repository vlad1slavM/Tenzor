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
                                           class_name="PopularRequestList-Item_pos_0")
        self.search_box = WebElement(self.driver, class_name="input__control")
        self.first_image = WebElement(self.driver, class_name="serp-item_pos_0")
        self.descriptions_field = WebElement(self.driver, class_name="MMSidebar-Container")
        self.open_image = WebElement(self.driver, class_name="MMImage-Origin")
        self.title_open_image = WebElement(self.driver, class_name="MMOrganicSnippet-Title")
        self.circle_button_next = WebElement(self.driver, class_name="CircleButton_type_next")
        self.circle_button_prev = WebElement(self.driver, class_name="CircleButton_type_prev")