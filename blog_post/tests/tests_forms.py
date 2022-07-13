import pytest
from blog_post.forms import CommentForm, PostForm, UpdateForm
from tests.tests_utils import TestCategoryUtils


@pytest.mark.parametrize(
    'content, valid, numb_of_errors',

    [('That looks nice!', True, 0), # Test field valid
     ('', False, 1), # Test field invalid
   ])


@pytest.mark.django_db
def test_comment_valid_form(content, valid, numb_of_errors):
    """
    Test  comment form validity.
    """
    form = CommentForm(
        data={
            'content': content,
        }
    )

    assert form.is_valid() is valid 
    assert len(form.errors) == numb_of_errors     


@pytest.mark.parametrize(
    'title, category_name, category_slug, content, post_img, meta_description, valid, numb_of_errors',

    [('New title', 'Test category', 'test-category', 'This is some test content', 'post_img.png', 'test', True, 0), # Test field valid
     ('', 'Test category', 'test-category', 'This is some test content', 'post_img.png', 'test', False, 1), # Test blank invalid title
     ('New title', 'Test category', 'test-category', '', 'post_img.png', 'test', False, 1), # Test blank invalid content
     ('New title', 'Test category', 'test-category', 'This is some test content', '', '', True, 0), # Test valid optional img
     ('New title', 'Test category', 'test-category', 'This is some test content', 'post_img.png', 'test', True, 0), # Test valid optional meta description
   ])


@pytest.mark.django_db
def test_post_valid_form(title, category_name, category_slug, content, post_img, meta_description, valid, numb_of_errors):
    """
    Test post form validity.
    """
    

    form = PostForm(
        data={
            "title": title,
            "category": TestCategoryUtils.create_test_category(category_name, category_slug),
            "content": content,
            "post_img": post_img,
            "meta_description": meta_description,
        }
    )

    assert form.is_valid() is valid 
    assert len(form.errors) == numb_of_errors    


@pytest.mark.parametrize(
    'title, category_name, category_slug, content, post_img, meta_description, valid, numb_of_errors',

    [('New title 1', 'Test category 1', 'test-category-1', 'This is some test content again', 'post_img.png', 'test', True, 0), # Test field valid
     ('', 'Test category 1', 'test-category-1', 'This is some test content again', 'post_img.png', 'test', False, 1), # Test blank invalid title
     ('New title 1', 'Test category 1', 'test-category-1', '', 'post_img.png', 'test', False, 1), # Test blank invalid content
     ('New title 1', 'Test category 1', 'test-category-1', 'This is some test content again', '', '', True, 0), # Test valid optional img
     ('New title 1', 'Test category 1', 'test-category-1', 'This is some test content again', 'post_img.png', 'test', True, 0), # Test valid optional meta description

   ])


@pytest.mark.django_db
def test_update_valid_form(title, category_name, category_slug, content, post_img, meta_description, valid, numb_of_errors):
    """
    Test  update form validity.
    """
    form = UpdateForm(
        data={
            "title": title,
            "category": TestCategoryUtils.create_test_category(category_name, category_slug),
            "content": content,
            "post_img": post_img,
            "meta_description": meta_description,
        }
    )

    assert form.is_valid() is valid 
    assert len(form.errors) == numb_of_errors 
