from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, View
from django.views import generic
from .models import Post, Like


class BlogPostDetail(generic.DetailView):

    def get(self, request, slug, *args, **kwargs):
        template_name = 'blog_post.html'
        queryset = Post.objects.filter(published=1).order_by('-created_on')

        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_post.html",
            {
                'post': post,
                'liked': liked,
            },
        )

def like_post(request, slug):
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


