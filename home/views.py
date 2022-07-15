from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.views import generic
from django.db.models import Q
from blog_post.models import Post, Category


class BlogPostList(ListView):
    """
    Used for showing posts and categories on homepage
    """

    model = Post
    template_name = "index.html"
    context_object_name = "index"
    paginate_by = 4

    # Inspiration from:
    # https://stackoverflow.com/questions/61022964/how-do-i-access-the-context-data-in-the-template
    def get_context_data(self, *args, **kwargs):
        context = super(BlogPostList, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()

        return context

    def get_queryset(self):
        all_published_posts = Post.objects.filter(
            published=1).order_by("-created_on")

        # Inspiration from:
        # https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
        if hasattr(self.request.user, "profile"):
            for post in all_published_posts:
                post.liked = False
                if post.likes.filter(id=self.request.user.profile.id).exists():
                    post.liked = True

        queryset = all_published_posts

        return queryset


class CategoryPostList(generic.ListView):
    """
    Used for showing posts that belongs to the same category
    """

    model = Post
    template_name = "posts_by_category.html"
    context_object_name = "posts_by_category"

    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        all_published_posts = Post.objects.filter(
            published=1, category=category
        ).order_by("-created_on")

        if hasattr(self.request.user, "profile"):
            for post in all_published_posts:
                post.liked = False
                if post.likes.filter(id=self.request.user.profile.id).exists():
                    post.liked = True

        context = {"post_list": all_published_posts, "category": category}

        return render(request, "posts_by_category.html", context)


# Inspiration from:
# https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query
class SearchResult(View):
    """
    Used for searching on post titles, content,
    category, and author or categories on site
    """

    def get(self, request):
        if request.method == "GET":
            search = request.GET["search"]
            # Filter on if post title,content or author
            # contains text from search box
            posts = Post.objects.filter(
                Q(title__contains=search, published=1) |
                Q(content__contains=search, published=1) |
                Q(category__name__contains=search, published=1) |
                Q(author__username__contains=search, published=1)
            )
            # Filter on if categories contains text from search box
            categories = Category.objects.filter(Q(name__contains=search))

            return render(
                request,
                "search_result.html",
                {"search": search, "posts": posts, "categories": categories},
            )
        else:
            return render(request, "search_result.html", {})
