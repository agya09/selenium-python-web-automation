import time
from my_package.elements import BasePageElement
from .locators import HomeLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

about_page_url = 'https://saucelabs.com/'

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

