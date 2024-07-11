import time
from .locators import *

login_page_url = 'https://www.saucedemo.com/v1/index.html'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class Login(BasePage):

    def wait(self,s):
        time.sleep(s)