from django.urls import path
from .views import BlogPostList, like_post_home, CategoryPostList
from . import views


urlpatterns = [
     # path('', HomeView.as_view(), name='index'),
     path('', views.BlogPostList.as_view(), name='index'),
     path('<slug:slug>/like/', like_post_home, name='post_likes'),
     path('category/<slug:slug>/', views.CategoryPostList.as_view(), name='post_by_category'),
]


