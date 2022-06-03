from django.shortcuts import render
from django.views.generic import ListView
from blog_post.models import Post


class HomeView(ListView):
    """ 
     Used for showing posts on homepage
     """
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(published=1).order_by('-created_on')
