from django.urls import path, re_path
from .views import BlogPostDetail, like_post, CreatePost
from . import views


urlpatterns = [
    # path('', views.BlogPostList.as_view(), name='index'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blog_post'),
    path('<slug:slug>/like/', like_post, name='post_likes'),
    
    
]