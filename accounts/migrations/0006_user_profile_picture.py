# Generated by Django 4.2.10 on 2024-04-25 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_disliked_genres_alter_user_liked_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default.png', upload_to='profile_pictures/'),
        ),
    ]