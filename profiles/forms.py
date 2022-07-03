from .models import Profile
from django import forms


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_email', 'profile_img')
