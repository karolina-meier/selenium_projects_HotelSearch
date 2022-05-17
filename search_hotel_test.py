from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element(By.XPATH, "//span[text()='Search by Hotel or City Name']").click()
driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element(By.XPATH,"//span[text()='Dubai']").click()
driver.find_element(By.NAME, "checkin").send_keys('01/01/2023')
driver.find_element(By.NAME, "checkout").send_keys('08/01/2023')
#method using calendary
#driver.find_element(By.NAME, "checkin").click()
#driver.find_element(By.XPATH, "//td[@class='day ' and text()='25']").click()
#elements = driver.find_elements(By.XPATH, "//td[@class='day ' and text()='27']")
#for element in elements:
#    if element.is_displayed():
#        element.click()
#        break
driver.find_element(By.ID, "travellersInput").click()
driver.find_element(By.ID, "adultInput").clear()
driver.find_element(By.ID, "adultInput").send_keys('3')
driver.find_element(By.ID, "childPlusBtn").click()
driver.find_element(By.XPATH, "//button[text()=' Search']").click()
hotels = driver.find_elements(By.XPATH, "//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)
prices = driver.find_elements(By.XPATH, "//div[contains(@class,'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Price: " + price)

assert hotel_names[0] == "Jumeirah Beach Hotel"
assert hotel_names[1] == "Oasis Beach Tower"
assert hotel_names[2] == "Rose Rayhaan Rotana"
assert hotel_names[3] == "Hyatt Regency Perth"

assert price_values[0] == '€20.24'
assert price_values[1] == '€46'
assert price_values[2] == '€73.60'
assert price_values[3] == '€138'

driver.quit()
