from django.urls import path
from .views import SettingsView
from . import views


urlpatterns = [
    path("<pk>/", views.SettingsView.as_view(), name="settings"),
]
