from django.urls import path
from .views import BlogPostList, CategoryPostList, SearchResult


urlpatterns = [
    path("", BlogPostList.as_view(), name="index"),
    path(
        "category/<slug:slug>/",
        CategoryPostList.as_view(),
        name="post_by_category",
    ),
    path("search/", SearchResult.as_view(), name="search"),
]
