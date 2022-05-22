from django.contrib import admin
from .models import Category, Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """This class is used for controlling what the Admin can see and do with posts"""
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
    """This class is used for controlling what the Admin can see and do with categorys"""
    model = Category

    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name', 'slug')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """This class is used for controlling what the Admin can see and do with comments"""
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

