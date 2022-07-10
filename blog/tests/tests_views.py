"""
Tests for blog app views
"""
import pytest
from django.urls import reverse
from blog_post.models import Post
from datetime import date
from blog_post.tests.tests_models import TestCategory


# Inspiration from: https://pytest-django.readthedocs.io/en/latest/helpers.html#client-django-test-client
def get_forced_login_test_user(client, django_user_model):
    username = "TestUser"
    password = "resUtseT"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)
    return user # Returns a user that is signed-in

# Tests that my blog list view return expected status code
@pytest.mark.django_db
def test_my_blog_list_view(client, django_user_model):
    user = get_forced_login_test_user(client, django_user_model)
    url = reverse('my_blog')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_view_returns_blog_post_list_as_expected(client, django_user_model):
    # Create a post that we can compare to what view returns.
    user = get_forced_login_test_user(client, django_user_model)
    category = TestCategory.create_test_category('Test category', 'test-category')
    post = Post.objects.create(
                title='Post Has No Likes',
                slug='post-has-no-likes',
                meta_description='nolikes',
                author=user,
                category=category,
                created_on=date.today(),
                updated_on=date.today(),
                content='I am a post with no likes or comments',
                published=0,
                post_img='default-image',
                )

    response = client.get(reverse('my_blog'))

    # Check context data frow view. A post created by user is by default not published.
    assert response.context['has_not_published_posts'] == True 
    assert response.context['has_published_posts'] == False
    assert response.context['category'].count() == 1
    assert response.context['category'].first() == category










