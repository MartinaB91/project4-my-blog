from django.shortcuts import render
from blog_post.models import Post, Category
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# class MyBlogPostList(LoginRequiredMixin, ListView):
#     """
#      Used for showing  users posts on "my blog page"
#      """
#     model = Post
#     template_name = 'my_blog.html'


class MyBlogPostList(ListView):
    """
    Used for showing  users posts on "my blog page".
    Both published and unpublished.
    """

    model = Post
    template_name = "my_blog.html"
    paginate_by = 6

    # Inspiration from:
    # https://stackoverflow.com/questions/61022964/how-do-i-access-the-context-data-in-the-template
    def get_context_data(self, *args, **kwargs):
        context = super(MyBlogPostList, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()

        return context

    def get_queryset(self):
        all_published_posts = Post.objects.order_by("-created_on")

        for post in all_published_posts:
            post.liked = False
            if post.likes.filter(id=self.request.user.profile.id).exists():
                post.liked = True

        queryset = all_published_posts

        return queryset
