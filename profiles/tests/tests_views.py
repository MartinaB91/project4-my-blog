import pytest
from django.urls import reverse
from django.test import RequestFactory
from tests.tests_utils import TestUserUtils
from profiles.views import SettingsView


@pytest.mark.django_db
def test_settings_view_context(client):
    """
    Tests settings view context values 
    """
    user = TestUserUtils.get_forced_login_test_user(client)
    url = reverse("settings", args=[user.id])
    response = client.get(url, follow=True)

    assert response.status_code == 200
    assert response.context['SettingsForm'].first_name == user.first_name 
    assert response.context['SettingsForm'].last_name == user.last_name


@pytest.mark.django_db 
def test_settings_view_queryset(client):
    """
    Test returned content of queryset
    """
    user = TestUserUtils.get_forced_login_test_user(client)

    request = RequestFactory()
    request.user = user  # Use our signed in user to make request
    request.get(reverse("settings", args=[user.id]))

    view = SettingsView()
    view.request = request

    queryset_result = view.get_queryset()  # get queryset data

    # Check that the queryset only contains 1 profile
    # and that it is the profile we created above
    assert queryset_result.count() == 1
    assert queryset_result.first() == user.profile

