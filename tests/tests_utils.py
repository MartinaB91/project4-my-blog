"""
Help methods for tests
"""

from django.contrib.auth.models import User
from blog_post.models import Category, Post
from profiles.models import Profile
from datetime import date


class TestUserUtils():
    """
    Used for creating a new user
    """
    def create_test_user(username, password):
        user = User.objects.create(
        username = username,
        password=password
        )
        return user

    # Inspiration from:
    # https://pytest-django.readthedocs.io/en/latest/helpers.html#client-django-test-client
    def get_forced_login_test_user(client):
        user = TestUserUtils.create_test_user("TestUser", "test123!!!!!")
        client.force_login(user)
        return user  # Returns a user that is signed-in


class TestProfileUtils():
    """
    Method used for creating a new profile 
    """
    def create_test_profile(username, test_first_name, test_last_name, password):
        user = TestUserUtils.create_test_user(username, password)
        profile = Profile.objects.create(
            user = user,
            first_name = test_first_name,
            last_name = test_last_name,
        )
        return profile


class TestPostUtils():
    """
    Creates a new post
    """
    def get_test_post():
        """
        Creates a new post 
        """
        user = TestUserUtils.create_test_user('RonjaRovardotter', 'passw000rd')
        category = TestCategoryUtils.create_test_category(
            'Flower Power',
            'flower-power'
            )
        post = Post.objects.create(
            title= 'Flower is nice',
            slug= 'flower-is-nice',
            meta_description= 'flower',
            author= user,
            category= category,
            created_on= date.today(),
            updated_on= date.today(),
            content= 'I really like my flowers',
            published= 0,
            post_img = 'default-image',
            )
        return post

class TestCategoryUtils():
    def create_test_category(test_name, test_slug): 
        """
        Method used for creating a new category
        """
        category = Category.objects.create(
        name = test_name,
        slug = test_slug,
            )
        return category

