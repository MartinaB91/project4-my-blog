import pytest
from blog_post.models import Category, Post
from profiles.tests.test_models import create_test_user, create_test_profile
from datetime import date

def create_test_category(test_name, test_slug):
    category = Category.objects.create(
    name = test_name,
    slug = test_slug,
    )
    return category

def get_test_post():
    user = create_test_user('AstridLindgren')
    category = create_test_category('Flower Power', 'flower-power')
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
  

@pytest.mark.django_db
def test_category_create():
    category = create_test_category('Flower Power', 'flower-power')
    assert category.name == 'Flower Power'
    assert category.slug == 'flower-power'
    assert category.category_img == 'default_image' # If no img is added

# Test when a new post is created, but not published.
@pytest.mark.django_db
def test_post_create():
    user = create_test_user('AstridLindgren')
    category = create_test_category('Flower Power', 'flower-power')
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
    assert post.author.username == 'AstridLindgren'
    assert post.category.name == 'Flower Power'
    assert str(post.created_on)[0:10] == str(date.today())
    assert str(post.updated_on)[0:10] == str(date.today())
    assert post.content == 'I really like my flowers'
    assert post.published == 0
    assert post.publish_date == None
    # assert post.likes == 
    assert post.number_of_likes == '0'
    assert post.liked == False
    assert post.post_img == 'default_image' # If no img is added


# @pytest.mark.django_db
# def test_comment_create():
#     post = get_test_post()
#     profile = create_test_profile('SelmaLagerlof', 'Selma', 'Lagerlof')#, 'default_img','selma@lagerlof.se')
#     comment = Comment.objects.create(
#         author = profile,
#         blog_post = post,
#         content = 'Really nice picture',
#         created_on= date.today(),
#         status = 'Unhandled',
#     )
#     assert comment.content == 'Really nice picture'
#     assert str(post.created_on)[0:10] == str(date.today())







