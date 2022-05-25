from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post


class BlogPostView(DetailView):
    model = Post
    template_name ='blog_post.html'
