from django.urls import path
from .views import BlogPostList, CategoryPostList, SearchResult
from . import views


urlpatterns = [
     path('', views.BlogPostList.as_view(), name='index'),
     path('category/<slug:slug>/', views.CategoryPostList.as_view(), name='post_by_category'),
     path('search/', views.SearchResult.as_view(), name='search'),
]


