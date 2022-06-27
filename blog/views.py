from django.shortcuts import render
from blog_post.models import Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class MyBlogPostList(LoginRequiredMixin, ListView):
    """ 
     Used for showing  users posts on "my blog page"
     """
    model = Post
    template_name = 'my_blog.html'

