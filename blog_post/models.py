from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from profiles.models import Profile


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
    category_img = CloudinaryField(
        "category_image",
        default="default_image",
    )

    class Meta:
        """
        Used for changing subcategory from categorys to categories
        """

        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    """
    Class used for blog posts.
    """

    PUBLISH_STATUS = ((0, "Draft"), (1, "Publish"))
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    meta_description = models.CharField(max_length=150, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post_author",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="post_category",
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    published = models.IntegerField(choices=PUBLISH_STATUS, default=0)
    publish_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(
        Profile, related_name="post_likes", default=[0], blank=True
    )
    number_of_likes = models.BigIntegerField(default="0")
    liked = models.BooleanField(default=False)
    post_img = CloudinaryField("post_image", default="default_image")

    class Meta:
        """
        Used for sorting posts on created date.
        """

        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("index")


class Comment(models.Model):
    """
    Class used for blog comments.
    """

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="comments_author",
    )
    blog_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="post_comments",
        blank=False,
        null=False,
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Used for sorting comments on created date.
        """

        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.author}: {self.blog_post}"
