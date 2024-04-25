from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from recommendations.choices import GENRES, TRIGGER_DICT, TRIGGERS

PREFERENCES = (
    ("like", "Like"),
    ("dislike", "Dislike"),
    ("block", "Block"),
    ("neutral", "No Preference"),
)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomRadioSelect(forms.RadioSelect):
    template_name = "accounts/row_radio_select.html"


class GenreForm(forms.Form):
    """
    This form is used to collect user preferences for each genre,
    the genre choices come from recommendations.choices.GENRES
    """

    def __init__(self, *args, **kwargs):
        initial_preferences = kwargs.pop("initial_preferences", {})
        super(GenreForm, self).__init__(*args, **kwargs)
        for genre in GENRES:
            genre_value = genre[0]
            genre_label = genre[1]
            self.fields[genre_value] = forms.ChoiceField(
                choices=PREFERENCES,
                label=genre_label,
                widget=CustomRadioSelect,
                required=False,
                initial=initial_preferences.get(genre_value, "neutral"),
            )

    def clean(self):
        cleaned_data = super(GenreForm, self).clean()
        for genre_value, _ in GENRES:  # Ensure at least one genre is not set to block
            preference = cleaned_data.get(genre_value)
            if preference != "block":
                return cleaned_data
        raise forms.ValidationError(
            "Not all genres can be set to 'Block'. Please choose different preferences for at least one genre."
        )


class CustomTriggerForm(forms.Form):
    """
    This form is used to collect user preferences for each trigger,
    """

    # TODO
