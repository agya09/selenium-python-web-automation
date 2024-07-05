import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.saucedemo.com/v1/inventory.html"


class HomePage(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)
        self.driver.maximize_window()

    def test_page_load(self):
        time.sleep(2)
        self.assertEqual(self.driver.current_url, url, "URL doesnot match")

    def tearDown(self):
        self.driver.close()


ele = HomePage()
ele.setUp()
ele.test_page_load()
ele.tearDown()
