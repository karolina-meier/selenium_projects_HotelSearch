import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class BaseTest:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()
