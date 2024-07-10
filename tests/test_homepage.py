import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from my_package.inventory import HomePage

url = "https://www.saucedemo.com/v1/inventory.html"
swag_url = "https://saucelabs.com/"


class Home(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(url)
        cls.driver.maximize_window()

    def test_1_page_load(self):
        screen = HomePage(self.driver)
        screen.wait(1)
        self.assertEqual(self.driver.current_url, url, "URL doesnot match")

    def test_2_right_sidebar(self):
        screen = HomePage(self.driver)
        screen.click_drawer()
        screen.wait(2)
        assert screen.drawer_is_clicked() is not None, "Right sidebar is loaded"

    def test_3_all_items_sidebar(self):
        screen = HomePage(self.driver)
        screen.wait(0.5)
        screen.click_all_items()
        screen.wait(1)
        self.assertEqual(self.driver.current_url, url, "All items are loaded")

    def test_4_about(self):
        screen = HomePage(self.driver)
        screen.click_drawer()
        screen.click_about()
        screen.wait(1)
        self.assertEqual(self.driver.current_url, swag_url, "Swag labs page is loaded.")
        self.driver.get(url)
    
    def test_5_logout(self):
        screen = HomePage(self.driver)
        

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
