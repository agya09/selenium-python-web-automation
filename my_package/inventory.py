import time
from .locators import HomeLocators

about_page_url = 'https://saucelabs.com/'
login_page_url = 'https://www.saucedemo.com/v1/index.html'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def wait(self,s):
        time.sleep(s)

    def is_home_page(self):
        return self.driver.find_element(*HomeLocators.LOGO)

    def click_drawer(self):
        ele = self.driver.find_element(*HomeLocators.DRAWER)
        ele.click()

    def drawer_is_clicked(self):
        return self.driver.find_element(*HomeLocators.DRAWER_SIDEBAR)

    def sidebar(self):
        return self.driver.find_element(*HomeLocators.SIDEBAR)

    def click_all_items(self):
        ele = self.driver.find_element(*HomeLocators.ALL_ITEMS)
        self.driver.implicitly_wait(10)
        # ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        ele.click()

    def click_about(self):
        ele = self.driver.find_element(*HomeLocators.ABOUT)
        ele.click()

    def is_about_page(self):
        return about_page_url

    def click_logout(self):
        self.driver.find_element(*HomeLocators.LOGOUT).click()

    def is_login_page(self):
        return login_page_url

    def click_close_icon(self):
        self.driver.find_element(*HomeLocators.CLOSE_ICON).click()

    def click_filter(self):
        self.driver.find_element(*HomeLocators.FILTER_BTN).click()

    def click_a_to_z(self):
        self.driver.find_element(*HomeLocators.SORT_A_TO_Z).click()

    def click_z_to_a(self):
        self.driver.find_element(*HomeLocators.SORT_Z_TO_A).click()

    def click_h_to_l(self):
        self.driver.find_element(*HomeLocators.SORT_PRICE_HIGH_TO_LOW).click()

    def click_l_to_h(self):
        self.driver.find_element(*HomeLocators.SORT_PRICE_LOW_TO_HIGH).click()

    def first_item(self):
        return self.driver.find_element(*HomeLocators.FIRST_ITEM).text
