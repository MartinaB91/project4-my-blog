from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        )
    category_img = CloudinaryField('image', default= '') #  TODO: Add a default picture

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_post_author',
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='blog_post_category',
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        Profile,
        related_name='blog_post_likes',
        blank=True,
        )
    post_img = CloudinaryField('image', default= '') #  TODO: Add a default picture

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.author}: {self.title}'


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='author_comments',
        )
    blog_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='blog_post_comments',
        blank=True,
        null=True,  # TODO: Read more about what to do about
        # 'It is impossible to add a non-nullable field'auto_created'auto_created'
        # https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.author}: {self.content}'


class Like(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='author_likes',
        )
    blog_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='blog_post_likes',
        )
