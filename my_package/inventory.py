import time
from my_package.elements import BasePageElement
from .locators import HomeLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

about_page_url = 'https://saucelabs.com/'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def wait(self):
        time.sleep(3)

    def is_home_page(self):
        return self.driver.find_element(*HomeLocators.LOGO)

    def click_drawer(self):
        ele = self.driver.find_element(*HomeLocators.DRAWER)
        ele.click()

    def drawer_is_clicked(self):
        return self.driver.find_element(*HomeLocators.DRAWER_SIDEBAR)

    def click_all_items(self):
        ele = self.driver.find_element(*HomeLocators.ALL_ITEMS)
        ele.click()

    def click_about(self):
        ele = self.driver.find_element(*HomeLocators.ABOUT)
        ele.click()

    def is_about_page(self):
        return about_page_url

