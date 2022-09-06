import pytest
import time
from pages.yandex_main_page import MainPage


@pytest.mark.usefixtures("setup")
class TestFirst:

    def test_second(self):
        page = MainPage(self.driver)
        assert page.search_field.is_visible() is True, "Поле ввода было не найдено"
        page.search_field.send_keys("Тензор")
        time.sleep(3)
        page.search_field.press_enter()
        time.sleep(3)
        hrefs = page.links_list.get_attributes("href")
        assert hrefs[0] == "https://tensor.ru/", "Первая ссылка ведет на сайт Тензора"



