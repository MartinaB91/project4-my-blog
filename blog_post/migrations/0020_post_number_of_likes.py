# Generated by Django 4.0.4 on 2022-06-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0019_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number_of_likes',
            field=models.BigIntegerField(default='0'),
        ),
    ]
