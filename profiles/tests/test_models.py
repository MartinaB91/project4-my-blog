import pytest
from tests.tests_utils import TestUserUtils

    
# Tests if user is created as expected
@pytest.mark.django_db
def test_user_create():
    test_user = TestUserUtils.create_test_user("AdaLovelace")
    assert test_user.username == "AdaLovelace"





   




