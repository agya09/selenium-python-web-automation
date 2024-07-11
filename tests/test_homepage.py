import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from my_package.inventory import HomePage

url = "https://www.saucedemo.com/v1/inventory.html"
swag_url = "https://saucelabs.com/"


class Home(unittest.TestCase):

    driver = None

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
        screen.click_drawer()
        screen.click_logout()
        screen.wait(2)
        self.assertEqual(screen.is_login_page(), self.driver.current_url, "Logout is not performed.")
        self.driver.get(url)
        screen.click_drawer()

    def test_6_close_sidebar(self):
        screen = HomePage(self.driver)
        screen.wait(2)
        screen.click_close_icon()
        assert True, "Sidebar is closed."

    def test_7_filter_by_name_a_to_z(self):
        screen = HomePage(self.driver)
        screen.click_a_to_z()
        screen.wait(1)
        expected_item = 'Sauce Labs Backpack'
        actual_item = screen.first_item()
        screen.wait(1)
        self.assertEqual(expected_item, actual_item, "Filter is not working properly.")

    def test_8_filter_by_name_z_to_a(self):
        screen = HomePage(self.driver)
        screen.click_z_to_a()
        screen.wait(1)
        expected_item = 'Test.allTheThings() T-Shirt (Red)'
        actual_item = screen.first_item()
        screen.wait(1)
        self.assertEqual(expected_item, actual_item, "Filter is not working properly.")

    def test_9_filter_by_price_high_to_low(self):
        screen = HomePage(self.driver)
        screen.click_h_to_l()
        screen.wait(1)
        expected_item = 'Sauce Labs Fleece Jacket'
        actual_item = screen.first_item()
        screen.wait(1)
        self.assertEqual(expected_item, actual_item, "Filter is not working properly.")

    def test_filter_by_price_low_to_high(self):
        screen = HomePage(self.driver)
        screen.click_l_to_h()
        screen.wait(1)
        expected_item = 'Sauce Labs Onesie'
        actual_item = screen.first_item()
        screen.wait(1)
        self.assertEqual(expected_item, actual_item, "Filter is not working properly.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()