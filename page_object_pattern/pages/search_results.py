from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import SearchResultLocators
import logging

class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = SearchResultLocators.hotel_names_xpath
        self.hotel_prices_xpath = SearchResultLocators.hotel_prices_xpath
        self.logger = logging.getLogger()

    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, self.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Available hotels are:")
        for name in names:
            self.logger.info(name)
        return names

    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, self.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Hotel prices:")
        for price in hotel_prices:
            self.logger.info(price)
        return hotel_prices
