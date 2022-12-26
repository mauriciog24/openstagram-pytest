from pages.auth.openstagram_login_page import OpenStagramLoginPage
from pages.openstagram_base_page import OpenStagramBasePage


def opst_verify_login_form_elements(browser, base_url):
    '''Verify login elements are displayed'''
    login_page = OpenStagramLoginPage(browser, base_url)
    login_page.load()
    # Header displayed
    assert login_page.find_login_on_openstagram_header() is not None
    # Email field
    assert login_page.find_email_label() is not None
    assert login_page.find_email_input() is not None
    # Password field
    assert login_page.find_password_label() is not None
    assert login_page.find_password_input() is not None
    # Remember Me checkbox
    assert login_page.find_remember_me_label() is not None
    assert login_page.find_remember_me_checkbox() is not None
    # Login button
    assert login_page.find_login_button() is not None


def opst_verify_login_navbar_buttons(browser):
    '''Verify the navbar buttons are the correct to be displayed'''
    base_page = OpenStagramBasePage(browser)
    # Buttons should be displayed
    assert base_page.find_home_button() is not None
    assert base_page.find_login_button() is not None
    assert base_page.find_register_button() is not None
    # Buttons shouldn't be displayed
    assert base_page.find_create_button() is None
    assert base_page.find_user_profile_button() is None
    assert base_page.find_logout_button() is None
