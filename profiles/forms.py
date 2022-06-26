from .models import Profile
from django import forms


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'profile_img')