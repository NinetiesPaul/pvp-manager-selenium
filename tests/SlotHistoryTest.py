from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.SetUp import *

"""
This test verifies that the Slot History functionality is working as expected.

Given the user selects an option from the slot 1 Pokemon dropdown,
that selected option should be added to the slot history drop down.
"""
class SlotHistoryTest(SetUp):
    testName = __name__.split(".")[1]
    outcome = ""

    def __init__(self):
        super().__init__(self.testName)
        self.run()
    
    def run(self):
        try:
            self.driver.find_element(By.ID, "select2-pokemonList_slot1-container").click()
            self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("Venusaur")
            self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)

            self.driver.find_element(By.ID, "select2-pokemonList_slot1-container").click()
            self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("Pikachu")
            self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)

            span_element = self.driver.find_element(By.CSS_SELECTOR, "#pokemonList_slot1_history > option:nth-child(2)")
            assert span_element.text == "0003 - Venusaur"

            self.outcome = "Test '" + self.testName + "' passed."

        except Exception as e:
            self.outcome = self.testName + "failed:", e

        self.close(self.outcome)
