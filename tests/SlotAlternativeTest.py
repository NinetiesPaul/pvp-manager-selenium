from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.SetUp import *

"""
This test verifies that the Slot Alternative functionality is working as expected.

Given the user selects an option from the slot 1 Pokemon dropdown,
the alternatives drop down should be filled with pokemon with similar typing
"""
class SlotAlternativeTest(SetUp):
    testName = __name__.split(".")[1]
    outcome = "Test '" + testName + "' passed."

    def __init__(self):
        super().__init__(self.testName)
        self.run()
    
    def run(self):
        try:
            self.driver.find_element(By.ID, "select2-pokemonList_slot1-container").click()
            self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("Steelix")
            self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)

            span_element = self.driver.find_element(By.CSS_SELECTOR, "#pokemonList_slot1_alternatives > option:nth-child(5)")
            assert span_element.text == "0530 - Excadrill", "Drop down doesn't have that option"

        except Exception as e:
            self.outcome = "Test '" + self.testName + "' failed:\n" + str(e)

        self.close(self.outcome)
