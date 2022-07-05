# Generated by Django 4.0.4 on 2022-07-05 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_rename_profile_email_profile_email'),
        ('blog_post', '0028_alter_like_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_author', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='like',
            name='blog_post',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to='blog_post.post'),
        ),
    ]