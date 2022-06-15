from django.urls import path, re_path
from .views import BlogPostDetail, like_post
from . import views


urlpatterns = [
    # path('', views.BlogPostList.as_view(), name='index'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blog_post'),
    path('<slug:slug>/like/', like_post, name='post_likes'),
]