from datetime import datetime
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views import generic
from .models import Post, Like, Comment
from .forms import CommentForm


class BlogPostDetail(generic.DetailView):

    def get(self, request, slug, *args, **kwargs):
        template_name = 'blog_post.html'
        queryset = Post.objects.filter(published=1).order_by('-created_on')
        post = get_object_or_404(queryset, slug=slug)

        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        context = {
            'post': post,
            'liked': liked,
        }

        return render(
            request,
            "blog_post.html",
            context,
        )

def like_post(request, slug):
    if request.method == 'POST':
        post_obj = get_object_or_404(Post, id=request.POST.get('post_id'))

        if post_obj.likes.filter(id=request.user.id).exists():
            post_obj.likes.remove(request.user.id)
            post_obj.number_of_likes -= 1
            post_obj.save()

        else:
            post_obj.likes.add(request.user.id)
            post_obj.number_of_likes += 1
            post_obj.save()

    return HttpResponse(post_obj.number_of_likes)
  