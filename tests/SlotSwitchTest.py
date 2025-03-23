from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.SetUp import *

"""
This test verifies that the Switch Slot Pokemon functionality is working as expected.

Given the user selects an option from the slot1 Pokemon dropdown,
then selects another option from the slot2 Pokemon dropdown,
then clicks the switchPositions labeled "1_and_2",
slot1 and slot2 selected options must switch between them
"""
class SlotSwitchTest(SetUp):
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

            self.driver.find_element(By.ID, "select2-pokemonList_slot2-container").click()
            self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("Pikachu")
            self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)

            self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(4) > .btn").click()

            span_element = self.driver.find_element(By.CSS_SELECTOR, "#select2-pokemonList_slot1-container")
            assert span_element.text == "0025 - Pikachu"

            self.outcome = "Test '" + self.testName + "' passed."

        except Exception as e:
            self.outcome = self.testName + "failed:", e

        self.close(self.outcome)
