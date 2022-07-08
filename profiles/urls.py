from django.urls import path
from .views import SettingsView


urlpatterns = [
    path("<pk>/", SettingsView.as_view(), name="settings"),
]
