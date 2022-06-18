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
#     queryset = Post.objects.filter(published=1).order_by('-created_on')

class BlogPostList(ListView):
    """ 
     Used for showing posts on homepage
     """
     
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(published=1).order_by('-created_on')

 
    def get_context_data(self, **kwargs):
        queryset = Post.objects.filter(published=1).order_by('-created_on')
        for post in queryset:  # Loop through all published posts 
            liked = False  
            if post.likes.filter(id=self.request.user.id).exists():  # If user has liked, set True. Todo: this dosen't work
                liked = True

        context = super().get_context_data(**kwargs)
        context['liked'] = liked
        
        return context

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
