# Generated by Django 4.2.10 on 2024-04-25 07:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0009_recommendation_recommended_films_alter_movie_genres_and_more'),
        ('accounts', '0006_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='excluded_films',
            field=models.ManyToManyField(blank=True, default=list, related_name='users_dont_recommend', to='recommendations.movie'),
        ),
        migrations.AddField(
            model_name='user',
            name='excluded_genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('History', 'History'), ('Horror', 'Horror'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Science Ficti', 'Science Fiction'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=13), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='user',
            name='rewatchable_films',
            field=models.ManyToManyField(blank=True, default=list, related_name='users_to_rewatch', to='recommendations.movie'),
        ),
        migrations.AddField(
            model_name='user',
            name='subscriptions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('', 'No Preference'), ('Amazon Prime Video', 'Amazon Prime Video'), ('Apple TV Plus', 'Apple TV Plus'), ('Criterion Channel', 'Criterion Channel'), ('Crunchyroll', 'Crunchyroll'), ('Disney Plus', 'Disney Plus'), ('Max', 'Max'), ('Hulu', 'Hulu'), ('MUBI', 'MUBI'), ('Netflix', 'Netflix'), ('Paramount Plus', 'Paramount Plus'), ('Peacock Premium', 'Peacock Premium'), ('Shudder', 'Shudder')], max_length=18), blank=True, default=list, size=None),
        ),
    ]
