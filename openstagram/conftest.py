from selenium import webdriver
from pytest import fixture


# Selenium config
DEFAULT_WAIT_TIME = 5
# Driver config
SUPPORTED_BROWSERS = ['chrome']
DRIVER_WIDTH = 1024
DRIVER_HEIGHT = 768


@fixture(scope='session')
def host(host='localhost'):
    '''Returns the host to be used in the execution'''
    protocol = 'http' if host == 'localhost' else 'https'
    return f'{protocol}://{host}'


@fixture(scope='session')
def port(port=8000):
    '''Returns the port to be used in the execution'''
    return port


@fixture(scope='session')
def base_url(host, port):
    '''Returns the base url to be used in the execution'''
    return f'{host}:{port}' if host == 'http://localhost' else host


@fixture(scope='module')
def browser(config_browser='chrome'):
    '''Initialize the webdriver'''
    if config_browser in SUPPORTED_BROWSERS:
        # Set some options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('-incognito')
        chrome_options.add_argument(f'--window-size={DRIVER_WIDTH},{DRIVER_HEIGHT}')
        # Initialize the driver
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        raise Exception(f'{config_browser} is not supported')
    # Wait for the elements to be ready
    driver.implicit_wait(DEFAULT_WAIT_TIME)
    # Return the driver
    yield driver
    # Quit the driver
    driver.quit()


@fixture(scope='function')
def user_login(browser):
    '''Logins as an user'''
    pass
