from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_img = CloudinaryField('profile_image', default='default_image')  #  TODO: Add a default picture

    def __str__(self):
        return f'{self.user}'