from django.urls import path
from .views import (
    BlogPostDetail,
    like_post,
    CreatePost,
    CreateComment,
    UpdatePost,
    DeletePost,
)


urlpatterns = [
    path("create_post/", CreatePost.as_view(), name="create_post"),
    path("<slug:slug>/update_post/", UpdatePost.as_view(), name="update_post"),
    path("<slug:slug>/delete_post/", DeletePost.as_view(), name="delete_post"),
    path("<slug:slug>/", BlogPostDetail.as_view(), name="blog_post"),
    path("<slug:slug>/like/", like_post, name="post_likes"),
    path(
        "<slug:slug>/create_comment/",
        CreateComment.as_view(),
        name="create_comment",
    ),
]
