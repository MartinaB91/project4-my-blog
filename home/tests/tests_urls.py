import pytest
from django.urls import reverse, resolve
from home.views import BlogPostList, CategoryPostList, SearchResult


def test_home_blog_post_list_url():
    """
    Tests the home blog post list url (home page)
    """
    url = reverse('index')
    assert resolve(url).func.view_class ==  BlogPostList


def test_category_post_list_url():
    """
    Tests post by category url 
    """
    url = reverse('post_by_category', args=['slug'])
    assert resolve(url).func.view_class ==  CategoryPostList

def test_search_result_url():
    """
    Tests search result url 
    """
    url = reverse('search')
    assert resolve(url).func.view_class ==  SearchResult