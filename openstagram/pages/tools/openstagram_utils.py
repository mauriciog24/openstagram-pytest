from time import sleep


class OpenStagramUtils:
    '''
    This class contains all the base methods needed for interact with the page
    '''
    def find_element(self, browser, locator):
        '''Finds an element in the page'''
        try:
            return browser.find_element(*locator)
        except:
            return None

    def fill_element(self, browser, locator, value, timeout=0):
        '''Fills an element in the page'''
        element = self.find_element(browser, locator)
        element.send_keys(value)
        sleep(timeout)

    def click_element(self, browser, locator, timeout=0):
        '''Clicks an element in the page'''
        element = self.find_element(browser, locator)
        try:
            element.click()
        except:
            pass # JavaScript click
        sleep(timeout)
