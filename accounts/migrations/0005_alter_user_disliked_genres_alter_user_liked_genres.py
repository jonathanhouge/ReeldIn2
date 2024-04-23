# Generated by Django 4.2.10 on 2024-04-22 20:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_seen_films_user_disliked_cast_and_crew_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='disliked_genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('History', 'History'), ('Horror', 'Horror'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Science Ficti', 'Science Fiction'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=13), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='liked_genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('History', 'History'), ('Horror', 'Horror'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Science Ficti', 'Science Fiction'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=13), blank=True, default=list, size=None),
        ),
    ]
