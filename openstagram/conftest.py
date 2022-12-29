from selenium.webdriver import Chrome, Firefox, ChromeOptions, FirefoxOptions
from pytest import fixture

from pages.auth.openstagram_register_page import OpenStagramRegisterPage
from pages.auth.openstagram_login_page import OpenStagramLoginPage


# Selenium config
DEFAULT_WAIT_TIME = 5
# Driver config
SUPPORTED_BROWSERS = ['chrome', 'firefox']
DRIVER_WIDTH = 1024
DRIVER_HEIGHT = 768


def pytest_addoption(parser):
    '''Defines parameters for the execution'''
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Browser to be used during the execution'
    )
    parser.addoption(
        '--host',
        action='store',
        default='localhost',
        help='Host to be used during the execution'
    )
    parser.addoption(
        '--port',
        action='store',
        default='8000',
        help='Port to be used during the execution'
    )


@fixture(scope='session')
def host(request):
    '''Returns the host to be used in the execution'''
    return request.config.getoption('--host')


@fixture(scope='session')
def port(request):
    '''Returns the port to be used in the execution'''
    return request.config.getoption('--port')


@fixture(scope='session')
def base_url(host, port):
    '''Returns the base url to be used in the execution'''
    return f'http://{host}:{port}' if host == 'localhost' else f'https://{host}'


@fixture(scope='module')
def browser(request):
    browser = request.config.getoption('--browser')
    '''Initialize the webdriver'''
    if browser not in SUPPORTED_BROWSERS:
        raise Exception(f'{browser} is not supported')
    # Setup the driver
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('-incognito')
        options.add_argument(f'--window-size={DRIVER_WIDTH},{DRIVER_HEIGHT}')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('-private')
        options.add_argument(f'--width={DRIVER_WIDTH}')
        options.add_argument(f'--height={DRIVER_HEIGHT}')
        driver = Firefox(options=options)
    # Wait for the elements to be ready
    driver.implicitly_wait(DEFAULT_WAIT_TIME)
    # Return the driver
    yield driver
    # Quit the driver
    driver.quit()


@fixture(scope='function')
def user_login(browser, base_url):
    '''Logins an user or register it'''
    user = {
        'name': 'User Test',
        'username': 'Test',
        'email': 'test@email.com',
        'password': 'pass123'
    }
    # Do login
    login_page = OpenStagramLoginPage(browser, base_url)
    login_page.load()
    login_page.do_login(user['email'], user['password'])
    # Check if User is registered
    if login_page.find_bad_credentials_label() is not None:
        # Do register
        register_page = OpenStagramRegisterPage(browser, base_url)
        register_page.load()
        register_page.do_register(user['name'], user['username'], user['email'], user['password'])
