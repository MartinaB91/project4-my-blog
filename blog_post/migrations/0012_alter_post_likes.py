# Generated by Django 4.0.4 on 2022-06-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_profile_img'),
        ('blog_post', '0011_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to='profiles.profile'),
        ),
    ]
