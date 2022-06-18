from django.urls import path, re_path
from .views import BlogPostDetail, like_post, CreatePost, CreateComment, UpdatePost, DeletePost
from . import views


urlpatterns = [
    # path('', views.BlogPostList.as_view(), name='index'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:slug>/update_post/', views.UpdatePost.as_view(), name='update_post'),
    path('<slug:slug>/delete_post/', views.DeletePost.as_view(), name='delete_post'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blog_post'),
    path('<slug:slug>/like/', like_post, name='post_likes'),     
    path('<slug:slug>/create_comment/', views.CreateComment.as_view(), name='create_comment'),
    
]