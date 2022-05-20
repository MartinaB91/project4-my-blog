from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Class used for blog categories.
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=False,
        null=False,
        )
    category_img = CloudinaryField('category_image', default= 'default_image') #  TODO: Add a default picture
    #  https://cloudinary.com/blog/placeholder_images_and_gravatar_integration_with_cloudinary

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    """
    Class used for blog posts.
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_author',
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='post_category',
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    published = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        Profile,
        related_name='post_likes',
        default=0,
        )
    post_img = CloudinaryField('post_image', default='default_image')  # TODO: Add a default picture

    class Meta:
        """
        Used for sorting posts on created date.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.author}: {self.title}'


class Comment(models.Model):
    """
    Class used for blog comments.
    """
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='comments_author',
        )
    blog_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_comments',
        blank=False,
        null=False,  # TODO: Read more about what to do about
        # 'It is impossible to add a non-nullable field'auto_created'auto_created'
        # https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Used for sorting comments on created date.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.author}: {self.content}'


class Like(models.Model):
    """
    Class used for blog likes
    """
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='likes_author',
        )
    blog_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_likes',
        )