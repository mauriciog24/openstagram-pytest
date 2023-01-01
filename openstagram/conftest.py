from selenium.webdriver import (
    Chrome, Edge, Firefox, ChromeOptions, EdgeOptions, FirefoxOptions
)
from pytest import fixture

from pages.posts.openstagram_create_post_page import OpenStagramCreatePostPage
from pages.profile.openstagram_dashboard_page import OpenStagramDashboardPage
from pages.auth.openstagram_register_page import OpenStagramRegisterPage
from pages.auth.openstagram_login_page import OpenStagramLoginPage
from pages.posts.openstagram_post_page import OpenStagramPostPage
from pages.openstagram_base_page import OpenStagramBasePage


# Selenium config
DEFAULT_WAIT_TIME = 5
# Driver config
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


@fixture(scope='module')
def browser(request, host, port):
    '''Initialize the webdriver'''
    browser = request.config.getoption('--browser')
    # Sets up the driver
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
    elif browser == 'edge':
        options = EdgeOptions()
        options.add_argument('inprivate')
        options.add_argument(f'--window-size={DRIVER_WIDTH},{DRIVER_HEIGHT}')
        driver = Edge(options=options)
    else:
        raise Exception(f'{browser} is not supported')
    # Waits for the elements to be displayed
    driver.implicitly_wait(DEFAULT_WAIT_TIME)
    # Return the driver and the base url
    yield driver, f'http://{host}:{port}'
    # Quit the driver
    driver.quit()


@fixture(scope='module')
def login(browser):
    '''Logs in an user or register it if doesn't exists'''
    user = {
        'name': 'User Test',
        'username': 'Test',
        'email': 'test@email.com',
        'password': 'pass123'
    }
    # Do login
    login_page = OpenStagramLoginPage(*browser)
    login_page.load()
    login_page.do_login(user['email'], user['password'])
    # Check if User is registered
    if login_page.find_bad_credentials_label() is not None:
        # Do register
        register_page = OpenStagramRegisterPage(*browser)
        register_page.load()
        register_page.do_register(user['name'], user['username'], user['email'], user['password'])


@fixture(scope='module')
def register(browser):
    '''Register a new user'''
    user = {
        'name': 'User Test2',
        'username': 'Test2',
        'email': 'test2@email.com',
        'password': 'pass123'
    }
    # Do register
    register_page = OpenStagramRegisterPage(*browser)
    register_page.load()
    register_page.do_register(user['name'], user['username'], user['email'], user['password'])
    # Check if User is registered
    if register_page.find_field_error_message('username', 'has already been taken') is None:
        # Logs out the created user
        base_page = OpenStagramBasePage(browser[0])
        base_page.click_logout_button(3)


@fixture(scope='module')
def new_post(browser):
    '''Sets up a new Post to verify comments section and teardown it'''
    create_post_page = OpenStagramCreatePostPage(*browser)
    create_post_page.load()
    create_post_page.do_create_post('Test Post Title', 'This is the description of the Test Post')
    dashboard_page = OpenStagramDashboardPage(*browser)
    dashboard_page.click_post_by_title('Test Post Title', 3)
    yield
    post_page = OpenStagramPostPage(*browser)
    post_page.click_delete_post_button(1)
