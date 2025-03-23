from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.SetUp import *
import time

"""
This test verifies that the 'Paste to Builder' button on the Team Assembler table result is working as expected.

Given the user enter a list of Pokemons on the .pkm-list element,
and clicks the "Create Team" button,
the app will retrieve a valid list of teams membered by the Pokemon chosen,
and each row of the table has a 'Paste to Builder' button that when clicked will send the team to the Team Builder slots and automatically switch to this Tab
"""
class PasteToBuilderTest(SetUp):
    testName = __name__.split(".")[1]
    outcome = "Test '" + testName + "' passed."

    def __init__(self):
        super().__init__(self.testName)
        self.run()

    def run(self):
        try:
            self.driver.find_element(By.ID, "pvp-teamassembler-tab").click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, ".pkm-list").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pkm-list").send_keys("Charizard,Venusaur,Blastoise")
            self.driver.find_element(By.CSS_SELECTOR, ".pkm-list-btn").click()
            
            self.driver.find_element(By.ID, "paste_pkms").click()
            
            time.sleep(3)

            slot1_element = self.driver.find_element(By.CSS_SELECTOR, "#select2-pokemonList_slot1-container")
            assert slot1_element.text == "0009 - Blastoise", "Slot 1 has an invalid Pokemon"
            slot2_element = self.driver.find_element(By.CSS_SELECTOR, "#select2-pokemonList_slot2-container")
            assert slot2_element.text == "0006 - Charizard", "Slot 2 has an invalid Pokemon"
            slot3_element = self.driver.find_element(By.CSS_SELECTOR, "#select2-pokemonList_slot3-container")
            assert slot3_element.text == "0003 - Venusaur", "Slot 3 has an invalid Pokemon"

        except Exception as e:
            self.outcome = "Test '" + self.testName + "' failed:\n" + str(e)

        self.close(self.outcome)
