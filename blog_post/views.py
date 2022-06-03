from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views import generic
from .models import Post


class BlogPostList(generic.ListView): # TODO: Maybe remove later on, maybe doing the same thing as HomeView
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(published=1).order_by('-created_on')


class BlogPostDetail(generic.DetailView):

    def get(self, request, slug, *args, **kwargs):
        template_name = 'blog_post.html'
        queryset = Post.objects.filter(published=1).order_by('-created_on')

        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "blog_post.html",
            {
                "post": post,
            },
        )
