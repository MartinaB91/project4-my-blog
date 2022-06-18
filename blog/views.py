from django.shortcuts import render
from blog_post.models import Post
from django.views.generic import ListView


# def my_blog(request):
#     return render(request, 'my_blog.html')

class MyBlogPostList(ListView):
    """ 
     Used for showing  users posts on "my blog page"
     """
    model = Post
    template_name = 'my_blog.html'

