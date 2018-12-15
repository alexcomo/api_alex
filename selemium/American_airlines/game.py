from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

import unittest
import time

class SelectOptionFb(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Firefox()
        self.driver.get("https://en11.forgeofempires.com/")

    def test_select(self):
        driver=self.driver
        driver.maximize_window()
        # dropDown="month"
        # mDropD = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(dropDown))
        # Select(mDropD).select_by_visible_text("May")
        time.sleep(8)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()