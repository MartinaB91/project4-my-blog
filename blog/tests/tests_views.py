"""
Tests for blog app views
"""
import pytest
from django.urls import reverse
from blog_post.models import Post
from blog.views import MyBlogPostList
from datetime import date
from blog_post.tests.tests_models import TestCategory
from django.test import RequestFactory
from tests.tests_utils import TestUserUtils


# Tests that my blog list view return expected status code
@pytest.mark.django_db
def test_my_blog_list_view_response(client, django_user_model):
    TestUserUtils.get_forced_login_test_user(client, django_user_model)
    url = reverse('my_blog')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_returns_my_blog_context(client, django_user_model):
    # Create a post that we can compare to what view returns.
    user = get_forced_login_test_user(client, django_user_model)
    category = TestCategory.create_test_category(
        'Test category', 'test-category'
        )
    Post.objects.create(
                title='New post',
                slug='new-post',
                meta_description='my new post',
                author=user,
                category=category,
                created_on=date.today(),
                updated_on=date.today(),
                content='I am a new post',
                published=0,
                post_img='default-image',
                )

    response = client.get(reverse('my_blog'))

    # Check context data frow view.
    # A post created by user is by default not published.
    assert response.context['has_not_published_posts'] is True
    assert response.context['has_published_posts'] is False
    assert response.context['category'].count() == 1
    assert response.context['category'].first() == category


@pytest.mark.django_db
def test_view_returns_my_blog_queryset(client, django_user_model):
    # Create a post that we can compare to what view returns.
    user = get_forced_login_test_user(client, django_user_model)
    category = TestCategory.create_test_category(
        'Test category', 'test-category'
        )
    post = Post.objects.create(
                title='New post',
                slug='new-post',
                meta_description='new post',
                author=user,
                category=category,
                created_on=date.today(),
                updated_on=date.today(),
                content='I am a new post',
                published=0,
                post_img='default-image',
                )

    request = RequestFactory()
    request.user = user  # Use our signed in user to make request
    request.get(reverse('my_blog'))

    view = MyBlogPostList()
    view.request = request

    queryset_result = view.get_queryset()  # get queryset data

    # Check that the queryset only contains 1 post
    # and that it is the post we created above
    assert queryset_result.count() == 1
    assert queryset_result.first() == post
