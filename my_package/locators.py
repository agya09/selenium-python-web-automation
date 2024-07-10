from selenium.webdriver.common.by import By

class HomeLocators(object):
    LOGO = (By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/div')
    DRAWER = (By.XPATH, '/html/body/div/div[1]/div/div[3]/div/button')
    DRAWER_SIDEBAR = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[1]')
    ALL_ITEMS = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/nav[1]/a[1]')
    ABOUT = (By.XPATH, '//*[@id="about_sidebar_link"]')
    LOGOUT = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    RESET_APP = (By.XPATH, '//*[@id="reset_sidebar_link"]')
    CLOSE_ICON = (By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div/button')
    CART_ICON = (By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/a')
    ADD_TO_CART = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button')
    REMOVE_BTN = (By.LINK_TEXT, 'REMOVE')
    FILTER_BTN = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select')
    SORT_A_TO_Z = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select/option[1]')
    SORT_Z_TO_A = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select/option[2]')
    SORT_PRICE_LOW_TO_HIGH = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select/option[3]')
    SORT_PRICE_HIGH_TO_LOW = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[1]/div[3]/select/option[4]')
