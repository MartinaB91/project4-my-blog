# Generated by Django 4.0.4 on 2022-07-14 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0031_remove_comment_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]