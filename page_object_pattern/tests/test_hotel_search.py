from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage
import allure
import pytest


@pytest.mark.usefixtures("setup")
class TestHotelSearch():

    @allure.title("Hotel search - test")
    @allure.description("Automation testing using Selenium with page object pattern")
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

        assert hotel_prices[0] == '€20.24'
        assert hotel_prices[1] == '€46'
        assert hotel_prices[2] == '€73.60'
        assert hotel_prices[3] == '€138'



