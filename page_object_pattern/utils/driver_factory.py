from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            return webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        raise Exception ("Provide valid driver name - Firefox or Chrom")
