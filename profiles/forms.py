from django import forms
from .models import Profile


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "email", "profile_img")
