from pytest import mark, param

from pages.auth.openstagram_register_page import OpenStagramRegisterPage


@mark.parametrize(
    'field',
    [
        param('name'),
        param('username'),
        param('email'),
        param('password')
    ]
)
def opst_verify_register_required_fields_message(browser, field):
    '''Verify the "field is required" message for the form fields'''
    register_page = OpenStagramRegisterPage(*browser)
    register_page.load()
    register_page.click_register_button()
    assert register_page.find_field_error_message(field, 'field is required') is not None


@mark.parametrize(
    'name,expected_result',
    [
        param('NameGreaterThanThirtyCharacters', 'must not be greater than 30 characters')
    ]
)
def opst_verify_register_valid_name(browser, name, expected_result):
    '''Verify the "must not be greater than 30 characters" message when name is invalid'''
    register_page = OpenStagramRegisterPage(*browser)
    register_page.load()
    register_page.fill_name_input(name)
    register_page.click_register_button()
    assert register_page.find_field_error_message('name', expected_result) is not None


@mark.parametrize(
    'username,expected_result',
    [
        param('SU', 'must be at least 3 characters'),
        param('UsernameGreaterThanTwentyCharacters', 'must not be greater than 20 characters')
    ]
)
def opst_verify_register_valid_username(browser, username, expected_result):
    '''
    Verify the "must be at least 3 characters" and "must not be greater than 20 characters"
    messages when username is invalid
    '''
    register_page = OpenStagramRegisterPage(*browser)
    register_page.load()
    register_page.fill_username_input(username)
    register_page.click_register_button()
    assert register_page.find_field_error_message('username', expected_result) is not None


@mark.parametrize(
    'email,expected_result',
    [
        param('invalidemail.com', 'must be a valid email address'),
        param('EmailFieldGreaterThanSixtyCharacters123456789012345@email.com', 'must not be greater than 60 characters')
    ]
)
def opst_verify_register_valid_email(browser, email, expected_result):
    '''
    Verify the "must be a valid email address" and "must not be greater than 60 characters"
    messages when email is invalid
    '''
    register_page = OpenStagramRegisterPage(*browser)
    register_page.load()
    register_page.fill_email_input(email)
    register_page.click_register_button()
    assert register_page.find_field_error_message('email', expected_result) is not None


@mark.parametrize(
    'password,password_confirmation,expected_result',
    [
        param('12345', '12345', 'must be at least 6 characters'),
        param('123456', '654321', 'confirmation does not match')
    ]
)
def opst_verify_register_valid_password(browser, password, password_confirmation, expected_result):
    '''
    Verify the "must be at least 6 characters" and "confirmation does not match"
    messages when password is invalid
    '''
    register_page = OpenStagramRegisterPage(*browser)
    register_page.load()
    register_page.fill_password_input(password)
    register_page.fill_password_confirmation_input(password_confirmation)
    register_page.click_register_button()
    assert register_page.find_field_error_message('password', expected_result) is not None
