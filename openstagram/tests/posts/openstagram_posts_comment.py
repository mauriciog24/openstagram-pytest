from pytest import mark, param

from pages.posts.openstagram_post_page import OpenStagramPostPage


def opst_verify_comment_form_elements(browser, setup_post):
    '''Verify comment section elements are displayed'''
    setup_post
    post_page = OpenStagramPostPage(*browser)
    assert post_page.find_add_comment_label() is not None
    assert post_page.find_comment_label() is not None
    assert post_page.find_comment_input() is not None
    assert post_page.find_comment_button() is not None
    assert post_page.find_no_comments_label() is not None


@mark.parametrize(
    'comment',
    [
        param('Test comment')
    ]
)
def opst_verify_successful_comment(browser, comment):
    '''Verify the successful submit of a Comment in a Post'''
    post_page = OpenStagramPostPage(*browser)
    post_page.fill_comment_input(comment)
    post_page.click_comment_button(1)
    assert post_page.find_successful_comment_label() is not None
    assert post_page.find_no_comments_label() is None
