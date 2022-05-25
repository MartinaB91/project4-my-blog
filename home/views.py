from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog_post.models import Post


class HomeView(ListView):
    """ 
    Used for showing posts on homepage
    """
    model = Post
    template_name = 'index.html'