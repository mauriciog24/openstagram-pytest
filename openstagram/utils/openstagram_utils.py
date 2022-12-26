from selenium.webdriver.common.keys import Keys
from platform import system
from time import sleep


class OpenStagramUtils:
    '''
    This class contains all the base methods needed for interact with the page
    '''

    def __init__(self, browser):
        '''Initialize the webdriver'''
        self.browser = browser
        self.ctrl_key = Keys.CONTROL if system() != 'Darwin' else Keys.COMMAND

    def load_page(self, url, timeout=0):
        '''Redirects to a specific page'''
        self.browser.get(url)
        sleep(timeout)

    def find_element(self, locator):
        '''Finds an element in the page'''
        try:
            return self.browser.find_element(*locator)
        except:
            return None

    def fill_element(self, locator, value, timeout=0):
        '''Fills an element in the page'''
        element = self.find_element(locator)
        element.send_keys(value)
        sleep(timeout)

    def clear_element(self, locator, timeout=0):
        '''Clears an element in the page'''
        self.fill_element(locator, self.ctrl_key + 'a', 1)
        self.fill_element(locator, Keys.BACKSPACE, timeout)

    def click_element(self, locator, timeout=0):
        '''Clicks an element in the page'''
        element = self.find_element(locator)
        try:
            element.click()
        except:
            self.browser.execute_script('arguments[0].click;', element)
        sleep(timeout)
