from django.urls import path
from .views import BlogPostList, BlogPostDetail, BlogPostLike
from . import views

urlpatterns = [
    path('', views.BlogPostList.as_view(), name='index'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blog_post'),
    path('like/<slug:slug>/', views.BlogPostLike.as_view(), name='post_likes'),


]