from django.urls import path
from .views import MyBlogPostList

urlpatterns = [
    path("posts/", MyBlogPostList.as_view(), name="my_blog"),
]
