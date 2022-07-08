import pytest
from django.urls import reverse


# Tests that home view return expected status code
@pytest.mark.django_db
def test_home_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

