from django.views.generic import ListView
from blog_post.models import Post, Category


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
        context["has_not_published_posts"] = Post.objects.filter(
            published=0, author=self.request.user).exists()
        context["has_published_posts"] = Post.objects.filter(
            published=1, author=self.request.user).exists()

        return context

    def get_queryset(self):
        all_published_posts = Post.objects.filter(
            author=self.request.user).order_by("-created_on")

        for post in all_published_posts:
            post.liked = False
            if post.likes.filter(id=self.request.user.profile.id).exists():
                post.liked = True

        queryset = all_published_posts

        return queryset
