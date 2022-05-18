from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import SearchHotelLocators
import logging
import allure


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger()

    @allure.step("Setting city name to '{1}'")
    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, SearchHotelLocators.location_match_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_city", attachment_type=AttachmentType.PNG)

    @allure.step("Setting date range from '{1}' to '{2}'")
    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting date range {} - {}".format(check_in, check_out))
        self.driver.find_element(By.NAME, SearchHotelLocators.check_in_input_name).send_keys(check_in)
        self.driver.find_element(By.NAME, SearchHotelLocators.check_out_input_name).send_keys(check_out)
        allure.attach(self.driver.get_screenshot_as_png(), name="date_range", attachment_type=AttachmentType.PNG)

    @allure.step("Setting number of travellers - '{1}' adults and '{2}' child ")
    def set_travellers(self, adults, child):
        self.logger.info("Setting travellers: {} adults and {} child".format(adults, child))
        self.driver.find_element(By.ID, SearchHotelLocators.travellers_input_id).click()
        self.driver.find_element(By.ID, SearchHotelLocators.adult_input_id).clear()
        self.driver.find_element(By.ID, SearchHotelLocators.adult_input_id).send_keys(adults)
        self.driver.find_element(By.ID, SearchHotelLocators.child_input_id).clear()
        self.driver.find_element(By.ID, SearchHotelLocators.child_input_id).send_keys(child)
        allure.attach(self.driver.get_screenshot_as_png(), name="num_travellers", attachment_type=AttachmentType.PNG)

    @allure.step("Performing search")
    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_btn_xpath).click()