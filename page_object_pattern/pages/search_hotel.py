from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import SearchHotelLocators

class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver

    def set_city(self, city):
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, SearchHotelLocators.location_match_xpath).click()

    def set_date_range(self, check_in, check_out):
        self.driver.find_element(By.NAME, SearchHotelLocators.check_in_input_name).send_keys(check_in)
        self.driver.find_element(By.NAME, SearchHotelLocators.check_out_input_name).send_keys(check_out)

    def set_travellers(self, adults, child):
        self.driver.find_element(By.ID, SearchHotelLocators.travellers_input_id).click()
        self.driver.find_element(By.ID, SearchHotelLocators.adult_input_id).clear()
        self.driver.find_element(By.ID, SearchHotelLocators.adult_input_id).send_keys(adults)
        self.driver.find_element(By.ID, SearchHotelLocators.child_input_id).clear()
        self.driver.find_element(By.ID, SearchHotelLocators.child_input_id).send_keys(child)

    def perform_search(self):
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_btn_xpath).click()