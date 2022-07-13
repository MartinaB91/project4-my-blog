import pytest
from tests.tests_utils import TestUserUtils
from profiles.models import Profile

@pytest.mark.django_db
def test_user_create():
    """ 
    Tests if user is created
    """
    test_user = TestUserUtils.create_test_user("AdaLovelace", "password123")
    assert test_user.username == "AdaLovelace"


@pytest.mark.django_db
def test_profile_create_when_user_created():
    """ 
    Test if profile is created when user is. 
    """ 
    assert Profile.objects.all().count() == 0 # No profiles should exist
    TestUserUtils.create_test_user("Blogger", "password123")
    assert Profile.objects.all().count() == 1 # After creating a user 1 profile should exist





   




