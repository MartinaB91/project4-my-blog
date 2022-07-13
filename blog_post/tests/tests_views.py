import pytest
from django.urls import reverse
from blog_post.models import Post
from tests.tests_utils import TestPostUtils, TestUserUtils


@pytest.mark.django_db
def test_create_post_view_response(client):
    """
    Test create a post view response
    """
    TestUserUtils.get_forced_login_test_user(client)
    url = reverse('create_post')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_post_view_response(client):
    """
    Test update a post view response
    """
    TestUserUtils.get_forced_login_test_user(client)
    post = TestPostUtils.get_test_post()
    url = reverse("update_post", args=[post.slug])
    response = client.get(url, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_post_view_response(client):
    """
    Test delete a post view response
    """
    TestUserUtils.get_forced_login_test_user(client)
    post = TestPostUtils.get_test_post()
    url = reverse("delete_post", args=[post.slug])
    response = client.get(url, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_blog_post_detail_context(client):
    post = TestPostUtils.get_test_post()
    # response = client.get(reverse('blog_post', args=[post.slug]))
    url = reverse("blog_post", args=[post.slug])
    response = client.get(url, follow=True)

    assert response.status_code == 200
    assert response.context['post'] == post
    assert response.context['liked'] is False




