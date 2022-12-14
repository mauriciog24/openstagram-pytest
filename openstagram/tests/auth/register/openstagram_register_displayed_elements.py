from pages.auth.openstagram_register_page import OpenStagramRegisterPage
from pages.openstagram_base_page import OpenStagramBasePage


def opst_verify_register_form_elements(browser, base_url):
    '''Verify register elements are displayed'''
    register_page = OpenStagramRegisterPage(browser, base_url)
    register_page.load()
    # Header displayed
    assert register_page.find_register_on_openstagram_header() is not None
    # Name field
    assert register_page.find_name_label() is not None
    assert register_page.find_name_input() is not None
    # Username field
    assert register_page.find_username_label() is not None
    assert register_page.find_username_input() is not None
    # Email field
    assert register_page.find_email_label() is not None
    assert register_page.find_email_input() is not None
    # Password field
    assert register_page.find_password_label() is not None
    assert register_page.find_password_input() is not None
    # Password Confirmation field
    assert register_page.find_password_confirmation_label() is not None
    assert register_page.find_password_confirmation_input() is not None
    # Register button
    assert register_page.find_register_button() is not None


def opst_verify_register_navbar_buttons(browser):
    '''Verify the navbar buttons are the correct to be displayed'''
    base_page = OpenStagramBasePage(browser)
    # Buttons should be displayed
    assert base_page.find_home_button() is not None
    assert base_page.find_login_button() is not None
    assert base_page.find_register_button() is not None
    # Button shouldn't be displayed
    assert base_page.find_create_button() is None
    assert base_page.find_user_profile_button() is None
    assert base_page.find_logout_button() is None
