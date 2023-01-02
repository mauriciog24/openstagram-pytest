from pytest import mark, param

from pages.auth.openstagram_login_page import OpenStagramLoginPage


@mark.parametrize(
    'field',
    [
        param('email'),
        param('password')
    ]
)
def opst_verify_login_required_fields_message(browser, field):
    '''Verify the "field is required" message for email and password'''
    login_page = OpenStagramLoginPage(*browser)
    login_page.load()
    login_page.click_login_button()
    assert login_page.find_field_error_message(field, 'field is required') is not None


@mark.parametrize(
    'email,expected_result',
    [
        param('invalidemail.com', 'must be a valid email address')
    ]
)
def opst_verify_login_valid_email_address(browser, email, expected_result):
    '''Verify the "must be a valid email address" message when email is invalid'''
    login_page = OpenStagramLoginPage(*browser)
    login_page.load()
    login_page.fill_email_input(email)
    login_page.click_login_button()
    assert login_page.find_field_error_message('email', expected_result) is not None


@mark.parametrize(
    'email,password',
    [
        param('user@unregistered.com', 'pass123')
    ]
)
def opst_verify_login_bad_credentials_message(browser, email, password):
    '''Verify the "Bad credentials" message when login fails'''
    login_page = OpenStagramLoginPage(*browser)
    login_page.load()
    login_page.fill_email_input(email)
    login_page.fill_password_input(password)
    login_page.click_login_button()
    assert login_page.find_bad_credentials_label() is not None
