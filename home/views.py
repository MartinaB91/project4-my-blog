from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, DetailView
from blog_post.models import Post
from django.views import generic
from django.http import HttpResponse

# class HomeView(ListView):
#     """ 
#      Used for showing posts on homepage
#      """
#     model = Post
#     template_name = 'index.html'


class BlogPostList(generic.ListView):
    """ 
     Used for showing posts on homepage
     """
    model = Post
    template_name = 'index.html'
    context_object_name = 'index'
    
    def get_queryset(self):
        all_published_posts = Post.objects.filter(published=1).order_by('-created_on')
        categories = Category.objects.all()

        queryset = {
            'all_published_posts': all_published_posts,
            'categories': categories,
        }

        return queryset
   

def like_post_home(request, slug):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)

        if post_obj.likes.filter(id=request.user.id).exists():
            post_obj.likes.remove(user.id)
            post_obj.number_of_likes -= 1
            post_obj.save()

        else:
            post_obj.likes.add(user.id)
            post_obj.number_of_likes += 1
            post_obj.save()

    return HttpResponse(post_obj.number_of_likes)
