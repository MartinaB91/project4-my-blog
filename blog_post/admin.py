from django.contrib import admin
from .models import Category, Post, Comment

admin.site.site_header = "My Garden Administration"

# Inspiration from:
# https://realpython.com/python-django-blog/#step-2-create-the-django-blog-admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    This class is used for controlling what the Admin can see,
    filter, edit and search for in admin posts list
    """

    model = Post

    list_display = (
        "title",
        "author",
        "category",
        "slug",
        "publish_date",
        "published",
    )

    list_filter = (
        "author",
        "category",
        "published",
        "publish_date",
    )

    list_display_links = ("title",)

    search_fields = (
        "title",
        "slug",
        "author",
        "content",
        "category",
    )

    prepopulated_fields = {"slug": ("title",)}

    exclude = ("updated_on",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class is used for controlling what the Admin can see,
    filter, edit and search for in admin categories list
    """

    model = Category

    list_display = ("name", "slug")
    list_filter = ("name",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class is used for controlling what the Admin can see,
    filter, edit and search for in admin comments list
    """

    model = Comment

    list_display = (
        "blog_post",
        "content",
        "status",
        "author",
        "created_on",
    )

    list_filter = (
        "status",
        "author",
        "created_on",
    )

    list_editable = (
        "content",
        "status",
    )
    search_fields = (
        "author",
        "created_on",
    )
