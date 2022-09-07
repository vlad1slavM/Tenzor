import pytest
import time
from pages.yandex import MainPage, ImagesPage


@pytest.mark.usefixtures("setup")
class TestFirst:

    # def test_second(self):
    #     page = MainPage(self.driver)
    #     assert page.search_field.is_visible() is True, "Поле ввода было не найдено"
    #     page.search_field.send_keys("Тензор")
    #     time.sleep(3)
    #     page.search_field.press_enter()
    #     time.sleep(3)
    #     hrefs = page.links_list.get_attributes("href")
    #     assert hrefs[0] == "https://tensor.ru/", "Первая ссылка ведет на сайт Тензора"

    def test_first(self):
        page = MainPage(self.driver)
        assert page.link_images.is_visible() is True, "Ссылка на картинки была не найдена"
        page.link_images.click()
        time.sleep(3)
        page.switch_to_next_page()
        time.sleep(3)
        url = page.get_current_url()
        assert "/".join(url.split("/")[:-1]) == "https://yandex.ru/images", "Переход на вкладку с картинками"
        image_page = ImagesPage(self.driver, url=url)
        time.sleep(3)
        image_page.first_categories.click()
        time.sleep(50)
