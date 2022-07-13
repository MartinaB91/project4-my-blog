import pytest
from django.urls import reverse, resolve
from blog_post.views import (
    BlogPostDetail,
    like_post,
    CreatePost,
    CreateComment,
    UpdatePost,
    DeletePost,
)


def test_blog_post_detail_url():
    """
    Tests blog post detail url 
    """
    url = reverse('blog_post', args=['slug'])
    assert resolve(url).func.view_class ==  BlogPostDetail

    
def test_like_post_url():
    """
    Tests like post url 
    """
    url = reverse('post_likes', args=['slug'])
    assert resolve(url).func ==  like_post


def test_create_post_url():
    """
    Tests create post url 
    """
    url = reverse('create_post')
    assert resolve(url).func.view_class == CreatePost


def test_create_comment_url():
    """
    Tests create comment url 
    """
    url = reverse('create_comment', args=['slug'])
    assert resolve(url).func.view_class == CreateComment


def test_update_post_url():
    """
    Tests update post url 
    """
    url = reverse('update_post', args=['slug'])
    assert resolve(url).func.view_class == UpdatePost


def test_delete_post_url():
    """
    Tests delete url 
    """
    url = reverse('delete_post', args=['slug'])
    assert resolve(url).func.view_class == DeletePost


