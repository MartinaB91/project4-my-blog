# Generated by Django 4.0.4 on 2022-07-05 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0023_post_liked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
