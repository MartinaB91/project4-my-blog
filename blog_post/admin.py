from django.contrib import admin
from .models import Category, Post, Comment

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
        'id',
        'author',
        'title',
        'category',
        'slug',
        'published',
        'publish_date',

    )

    list_filter = (
        'author',
        'category',
        'published',
        'publish_date',
    )

    list_editable = (
        'title',
        'category',
        'publish_date',
        'published',
    )

    search_fields = (
        'title',
        'slug',
        'author',
        'content',
        'category',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class is used for controlling what the Admin can see,
    filter, edit and search for in admin categories list
    """
    model = Category

    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name', 'slug')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class is used for controlling what the Admin can see,
    filter, edit and search for in admin comments list
    """
    model = Comment

    list_display = (
        'blog_post',
        'content',
        'author',
        'created_on',
        'approved',

        )
    
    list_filter = (
        'blog_post',
        'author',
        'created_on',
        'approved',
    )

    list_editable = ('content', 'approved',)
    search_fields = ('author', 'created_on',)

