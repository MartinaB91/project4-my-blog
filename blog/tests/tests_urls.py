import pytest
from django.urls import reverse, resolve
from blog.views import MyBlogPostList

def test_my_blog_post_list_url():
    """
    Test my blog post list url 
    """
    url = reverse('my_blog')
    assert resolve(url).func.view_class == MyBlogPostList
