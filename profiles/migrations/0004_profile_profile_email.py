# Generated by Django 4.0.4 on 2022-07-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
