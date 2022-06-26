from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView


class SettingsView(ListView):
    """ 
     Used for showing settings page
     """
    model = Profile
    template_name = 'user_settings.html'
