import pytest
import time
from pages.yandex import MainPage, ImagesPage


@pytest.mark.usefixtures("setup")
class TestFirst:

    def test_search_yandex(self):
        page = MainPage(self.driver)
        assert page.search_field.is_visible() is True, "Поле ввода было не найдено"
        page.search_field.send_keys("Тензор")
        page.search_field.press_enter()
        hrefs = page.links_list.get_attributes("href")
        assert hrefs[0] == "https://tensor.ru/", "Первая ссылка ведет на сайт Тензора"

    def test_image_yandex(self):
        page = MainPage(self.driver)
        assert page.link_images.is_visible() is True, "Ссылка на картинки была не найдена"
        page.link_images.click()
        page.switch_to_next_page()
        url = page.get_current_url()
        assert "/".join(url.split("/")[:-1]) == "https://yandex.ru/images", "Переход на вкладку с картинками"
        image_page = ImagesPage(self.driver, url=url)
        image_page.first_categories.click()
        category_name = image_page.first_categories.get_text()
        input_text = image_page.search_box.get_attribute("value")
        assert category_name == input_text, "Навзание категории есть в поле поиска"
        image_page.first_image.click()
        assert image_page.descriptions_field.is_visible() is True, "Первая картинка была открыта"
        first_open_image = image_page.title_open_image.get_text()
        image_page.circle_button_next.click()
        time.sleep(1)
        second_open_image = image_page.title_open_image.get_text()
        assert first_open_image != second_open_image, "Картинка в открытом окне изменилась"
        image_page.circle_button_prev.click()
        assert image_page.title_open_image.get_text() == first_open_image,\
            "Картинка после перелистывания не изменилась"
