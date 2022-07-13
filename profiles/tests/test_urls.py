import pytest
from django.urls import reverse, resolve
from profiles.views import SettingsView


def test_profile_settings_url():
    """
    Tests the profile settings url 
    """
    url = reverse('settings', args=['pk'])
    assert resolve(url).func.view_class ==  SettingsView
