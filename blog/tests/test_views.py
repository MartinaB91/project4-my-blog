"""
Tests for blog app views
"""
import pytest
from django.urls import reverse

# Tests that my blog list view return expected status code
@pytest.mark.django_db
def test_my_blog_list_view(client):
    url = reverse('my_blog')
    response = client.get(url)
    assert response.status_code == 200