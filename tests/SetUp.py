from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SetUp():
    driver = None

    def __init__(self, testName):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )

        self.driver.maximize_window()
        self.driver.get("https://ninetiespaul.github.io/pvp-manager/")
        print("Test '" + testName + "' execution started.")
    
    def close(self, outcome):
        self.driver.close()
        self.driver.quit()

        print(outcome)
