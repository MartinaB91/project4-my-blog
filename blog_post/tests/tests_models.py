import pytest
from blog_post.models import Category, Post, Comment
from profiles.tests.test_models import create_test_user, create_test_profile
from datetime import date
from django.test import TestCase 

class TestCategory(TestCase):
# Category create helper function
    def create_test_category(test_name, test_slug): 
        category = Category.objects.create(
        name = test_name,
        slug = test_slug,
        )
        return category

    # Creates four categories and checks number of categories is as expected
    @pytest.mark.django_db
    def test_create_multiple_category(self):
        category_one = TestCategory.create_test_category('Cat One', 'cat-one')
        category_two = TestCategory.create_test_category('Cat Two', 'cat-two')
        category_three = TestCategory.create_test_category('Cat Three', 'cat-three')
        category_four = TestCategory.create_test_category('Cat Four', 'cat-four')

        assert Category.objects.all().count() == 4

    # Test create and remove a category 
    @pytest.mark.django_db
    def test_delete_category(self):
        category_to_delete = TestCategory.create_test_category('Del ete', 'del-ete')
        assert Category.objects.all().count() == 1
        category_to_delete.delete()
        assert Category.objects.all().count() == 0

    # Create a category
    @pytest.mark.django_db
    def test_category_create(self):
        category = TestCategory.create_test_category('Flower Power', 'flower-power')
        assert category.name == 'Flower Power'
        assert category.slug == 'flower-power'
        assert category.category_img == 'default_image' # If no img is added


class TestPost(TestCase):
    def setup():
        @pytest.fixture
        def get_test_post():
            user = create_test_user('RonjaRovardotter')
            category = TestCategory.create_test_category('Flower Power', 'flower-power')
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
                # published_date = date.today(),
                post_img = 'default-image',
                )
            return post

    # Test when a new post is created, but not published.
    @pytest.mark.django_db
    def test_post_create(self):
        user = create_test_user('PippiLongstockings')
        category = TestCategory.create_test_category('Flower Power', 'flower-power')
        post = Post.objects.create(
            title= 'Flower',
            slug= 'flower',
            meta_description= 'flower',
            author= user,
            category= category,
            created_on= date.today(),
            updated_on= date.today(),
            content= 'I really like my flowers',
            published= 0,
        )
        assert post.title == 'Flower'
        assert post.slug == 'flower'
        assert post.meta_description == 'flower'
        assert post.author.username == 'PippiLongstockings'
        assert post.category.name == 'Flower Power'
        assert str(post.created_on)[0:10] == str(date.today())
        assert str(post.updated_on)[0:10] == str(date.today())
        assert post.content == 'I really like my flowers'
        assert post.published == 0
        assert post.publish_date == None
        assert post.likes.count() == 0
        assert post.number_of_likes == '0'
        assert post.liked == False
        assert post.post_img == 'default_image' # If no img is added












