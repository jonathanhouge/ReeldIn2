from .models import Movie, Recommendation
from .choices import LANGUAGES
from django.db.models import Count


# creates a new recommendation model and sets it up
def make_new_recommendation(user):
    recommendation = Recommendation(user_id=user)
    recommendation.save()  # needs id

    all_movies = Movie.objects.all()
    recommendation.possible_films.set(all_movies)
    recommendation.possible_film_count = len(all_movies)
    recommendation.save()
    return recommendation


# makes sure the user only sees relevant options (only for languages so far)
# note: chatgpt helped make this way more efficient - was querying the db too much
def relevant_options(form, possible_films, possible_films_count):
    relevant_languages = [form.OPTIONS[0]]  # always have 'no preference'
    films_covered = 0

    # Annotate the queryset with the count of films for each language
    annotated_films = possible_films.values("language").annotate(num_films=Count("id"))

    for language_code, language_name in form.OPTIONS:
        # Find the count of films for the current language
        language_count = next(
            (
                entry["num_films"]
                for entry in annotated_films
                if entry["language"] == language_code
            ),
            0,
        )

        if language_count:
            relevant_languages.append((language_code, language_name))
            films_covered += language_count

        if films_covered == possible_films_count:
            break  # stop early if possible

    return relevant_languages


# TODO only works for genre, year, runtime, language
def recommendation_querying(recommendation, field, selection):
    if field == "year" or field == "runtime":
        span = selection.split("-")
        return recommendation.possible_films.filter(
            **{f"{field}__gte": span[0]}, **{f"{field}__lte": span[1]}
        )
    elif field == "language":
        if "" in selection:
            return recommendation.possible_films.all()  # user has no pref
        return recommendation.possible_films.filter(language__in=selection)

    # genre
    return recommendation.possible_films.filter(**{f"{field}__contains": selection})


# make arrays strings, make choices human readable, etc.
def make_readable_recommendation(recommended_films):
    readable_recommendation = []
    for film in recommended_films:
        readable_film = {
            "id": film.id,
            "name": film.name,
            "poster": film.poster,
            "year": film.year,
            "language": "",
            "genre": "",
            "director": "",
        }

        language_dict = dict(LANGUAGES)  # thanks chatgpt
        readable_film["language"] = language_dict.get(film.language)

        readable_film["genres"] = (", ").join(film.genres)
        readable_film["director"] = (", ").join(film.director)

        readable_recommendation.append(readable_film)

    return readable_recommendation
