from django.urls import path
from . import views
from . views import MyBlogPostList

urlpatterns = [
    # path('', views.my_blog, name='my_blog'),
    path('posts/', views.MyBlogPostList.as_view(), name='my_blog'),
]