# Generated by Django 4.0.4 on 2022-06-11 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0021_post_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
    ]
