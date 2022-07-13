import pytest
from django.urls import reverse
from blog_post.models import Post
from tests.tests_utils import TestUserUtils, TestCategoryUtils, TestPostUtils
from datetime import date
from django.test import RequestFactory
from home.views import BlogPostList


# Tests that home view return expected status code
@pytest.mark.django_db
def test_home_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_blog_post_list_view_context(client):
    """
    Tests context data response in blog_post_list view.
    """
    # Create a post that we can compare to what view returns.
    post = TestPostUtils.get_test_post()

    response = client.get(reverse('index'))

    assert response.context['category'].count() == 1
    assert response.context['category'].first() == post.category


@pytest.mark.django_db
def test_view_returns_blog_post_list_queryset(client):
    """
    Test returned content of queryset
    """
    user = TestUserUtils.get_forced_login_test_user(client)
    category = TestCategoryUtils.create_test_category(
    'Test category', 'test-category'
    )
    # Create a post that we can compare to what view returns.
    post = Post.objects.create(
            title='New post',
            slug='new-post',
            meta_description='new post',
            author=user,
            category=category,
            created_on=date.today(),
            updated_on=date.today(),
            content='I am a new post',
            published=1,
            post_img='default-image',
            )
    request = RequestFactory()
    request.user = user  # Use our signed in user to make request
    request.get(reverse('index'))

    view = BlogPostList()
    view.request = request

    queryset_result = view.get_queryset()  # get queryset data

    # Check that the queryset only contains 1 post
    # and that it is the post we created above
    assert queryset_result.count() == 1 # Expect one published post
    assert queryset_result.first() == post 


# Tests that home view return expected status code
@pytest.mark.django_db
def test_category_post_list_view(client):
    """
    Tests category post list view response 
    """
    category = TestCategoryUtils.create_test_category('test', 'test')
    url = reverse('post_by_category', args=[category.slug])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_category_post_list_view_context(client):
    """
    Tests context data response in blog_post_list view.
    """
    # Create a post that we can compare to what view returns.
    category = TestCategoryUtils.create_test_category('test', 'test')
    url = reverse('post_by_category', args=[category.slug])
    response = client.get(url)


    assert response.context['post_list'].count() == 0 # No posts created
    assert response.context['category'] == category


