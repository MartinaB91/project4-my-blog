from django.urls import path
from .views import BlogPostView

urlpatterns = [
    path('post/<slug:slug>', BlogPostView.as_view(), name='blog_post'),
]