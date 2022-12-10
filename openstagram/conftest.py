from selenium import webdriver
from pytest import fixture


# Selenium config
DEFAULT_WAIT_TIME = 5
# Driver config
SUPPORTED_BROWSERS = ['chrome']
DRIVER_WIDTH = 1024
DRIVER_HEIGHT = 768


def pytest_addoption(parser):
    '''Defines parameters for the execution'''
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
    pass # TODO: Implements login fixture
