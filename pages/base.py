from selenium import webdriver
import time


class WebBase:

    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_links(self):
        pass

    def get(self, url):
        self.driver.get(url)
        time.sleep(5)

    def refresh(self):
        self.driver.refresh()

    def switch_to_next_page(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
