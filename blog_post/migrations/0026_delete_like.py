# Generated by Django 4.0.4 on 2022-07-05 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0025_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
