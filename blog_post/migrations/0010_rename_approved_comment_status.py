# Generated by Django 4.0.4 on 2022-05-25 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0009_alter_comment_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved',
            new_name='status',
        ),
    ]