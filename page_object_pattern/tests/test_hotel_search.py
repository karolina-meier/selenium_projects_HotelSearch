from selenium import webdriver
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage

import pytest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range('01/01/2023', '08/01/2023')
        search_hotel_page.set_travellers('3', '1')
        search_hotel_page.perform_search()
        result_page = SearchResultsPage(self.driver)
        hotel_names = result_page.get_hotel_names()
        hotel_prices = result_page.get_hotel_prices()

        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        assert hotel_prices[0] == '$22'
        assert hotel_prices[1] == '$50'
        assert hotel_prices[2] == '$80'
        assert hotel_prices[3] == '$150'



