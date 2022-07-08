import pytest
from django.contrib.auth.models import User
from profiles.models import Profile

# Creating a user to be able to do other tests.

def create_test_user(test_username):
    user = User.objects.create(
    username=test_username,
    )
    return user

def create_test_profile(username, test_first_name, test_last_name):#, test_img, test_email):
    user = create_test_user(username)
    profile = Profile.objects.create(
        user = user,
        first_name = test_first_name,
        last_name = test_last_name,
        # profile_image = test_img,
        # email = test_email,
    )
    
# Tests if user is created as expected
@pytest.mark.django_db
def test_user_create():
    test_user = create_test_user("AdaLovelace")
    assert test_user.username == "AdaLovelace"





   




