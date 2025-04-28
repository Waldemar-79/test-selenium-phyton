import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_google_search(self):
        self.driver.get("http://www.google.de/xhtml")
        self.assertIn("Google", self.driver.title)
        time.sleep(5)

        search_field = self.driver.find_element(By.ID, "APjFqb")
        search_field.send_keys('google')
        search_field.send_keys(Keys.ENTER)
        assert "Es wurden keine mit deiner Suchanfrage!!" not in self.driver.page_source
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
