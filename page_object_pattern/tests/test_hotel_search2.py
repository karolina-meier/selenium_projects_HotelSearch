from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage
import allure
import pytest

#this test should failed
@pytest.mark.usefixtures("setup")
class TestHotelSearch2():

    @allure.title("Hotel search - test2")
    @allure.description("Automation testing using Selenium with page object pattern - this test should have assertion error ")
    def test_hotel_search2(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city2("London")
        search_hotel_page.set_date_range('12/12/2022', '14/12/2022')
        search_hotel_page.set_travellers('2', '0')
        search_hotel_page.perform_search()
        result_page = SearchResultsPage(self.driver)
        hotel_names = result_page.get_hotel_names()
        hotel_prices = result_page.get_hotel_prices()

        assert hotel_names[0] == "Grand Plaza Apartments"
        assert hotel_prices[0] == '$22'
