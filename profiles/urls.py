from django.urls import path
from .views import SettingsView
from . import views


urlpatterns = [
    path('', views.SettingsView.as_view(), name='settings'),
    
]