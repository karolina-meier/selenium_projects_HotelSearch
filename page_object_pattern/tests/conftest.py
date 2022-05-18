import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(request):
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()