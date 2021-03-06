from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.template.defaultfilters import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm, UpdateForm


class BlogPostDetail(DetailView):
    """
    Used for showing a single published post on blog post detail page.
    """
    template_name = "blog_post_detail.html"

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(published=1).order_by("-created_on")
        post = get_object_or_404(queryset, slug=slug)

        liked = False
        if hasattr(self.request.user, "profile"):
            if post.likes.filter(id=request.user.profile.id).exists():
                liked = True

        context = {
            "post": post,
            "liked": liked,
        }

        return render(
            request,
            "blog_post_detail.html",
            context,
        )


def like_post(request, slug):
    """
    Used for liking a post on blog post detail page
    """
    if request.method == "POST":
        post_obj = get_object_or_404(Post, id=request.POST.get("post_id"))

        if post_obj.likes.filter(id=request.user.profile.id).exists():
            post_obj.likes.remove(request.user.profile)
            post_obj.number_of_likes -= 1
            post_obj.save()

        else:
            post_obj.likes.add(request.user.profile)
            post_obj.number_of_likes += 1
            post_obj.save()

    return HttpResponse(post_obj.number_of_likes)


class CreatePost(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    """
    Used for creating a post
    """
    model = Post
    form_class = PostForm
    template_name = "create_post.html"

    def post(self, request):
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = self.request.user
                new_post.slug = slugify(new_post.title)
                new_post.save()
                messages.success(
                    self.request,
                    "Your post has been successfully created\
                        and will be published after review!",
                )
        form = PostForm()
        return redirect("my_blog")


class CreateComment(LoginRequiredMixin, CreateView):
    """
    Used for creating a comment
    """
    model = Comment
    form_class = CommentForm
    template_name = "comments.html"

    def post(self, request, slug):
        if request.method == "POST":

            queryset = Post.objects.filter(published=1).order_by("-created_on")
            post_obj = get_object_or_404(queryset, slug=slug)

            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.blog_post = post_obj
                new_comment.author = request.user.profile
                new_comment.slug = slug
                new_comment.save()
        form = CommentForm()
        return HttpResponse("Comment saved")


class UpdatePost(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    """
    Used for updating a post
    """
    model = Post
    form_class = UpdateForm
    template_name = "update_post.html"
    success_message = "Your post has been succsessfully updated!"

    def get_success_url(self):
        message_string = "Your post has been updated!"
        messages.success(self.request, message_string)
        return reverse_lazy("my_blog")


class DeletePost(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    """
    Used for deleting a post
    """
    model = Post
    template_name = "delete_post.html"

    def get_success_url(self):
        messages.success(self.request, "Your post has been deleted!")
        return reverse_lazy("my_blog")
