from pages.auth.openstagram_login_page import OpenStagramLoginPage


def opst_verify_login_required_fields_message(browser, base_url):
    '''Verify the "field is required" message for email and password'''
    login_page = OpenStagramLoginPage(browser, base_url)
    login_page.load()
    login_page.click_login_button()
    assert login_page.find_field_error_message('email', 'field is required') is not None
    assert login_page.find_field_error_message('password', 'field is required') is not None


def opst_verify_login_valid_email_address(browser, base_url):
    '''Verify the "must be a valid email address" message when email is invalid'''
    login_page = OpenStagramLoginPage(browser, base_url)
    login_page.load()
    login_page.fill_email_input('invalidemail.com')
    login_page.click_login_button()
    assert login_page.find_field_error_message('email', 'must be a valid email address') is not None


def opst_verify_login_bad_credentials_message(browser, base_url):
    '''Verify the "Bad credentials" message when login fails'''
    login_page = OpenStagramLoginPage(browser, base_url)
    login_page.load()
    login_page.fill_email_input('user@noregistered.com')
    login_page.fill_password_input('pass123')
    login_page.click_login_button()
    assert login_page.find_bad_credentials_label() is not None
