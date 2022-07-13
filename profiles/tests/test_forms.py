import pytest
from profiles.forms import SettingsForm


@pytest.mark.parametrize(
    'first_name, last_name, email, profile_img, valid, numb_of_errors',

    [('Mio', 'Minmio', 'mio@minmio.se', 'profile_img', True, 0), # Test all fields valid
    ('', 'Minmio', 'mio@minmio.se', 'profile_img', False, 1), # Test invalid firstname
    ('Mio', '', 'mio@minmio.se', 'profile_img', False, 1), # Test invalid lastname
    ('Mio', 'Minmio', '', 'profile_img', True, 0), # Test valid blank optional email
    ('Mio', 'Minmio', 'mail@mailcom', 'profile_img', False, 1), # Test invalid format email
    ('Mio', 'Minmio', 'mio@minmio.se', '', True, 0), # Test valid blank optional img
    ('', '', 'mio@minmio', '', False, 3), # Test all possible(not blank) invalid fields

    ]
)

@pytest.mark.django_db
def test_settings_valid_form(first_name, last_name, email, profile_img, valid, numb_of_errors):
    """
    Test SettingsForm with valid data
    """
    form = SettingsForm(
        data={
            "first_name": first_name,
            "last_name": last_name,
            "email": email, 
            "profile_img": profile_img,
        }
    )

    assert form.is_valid() is valid 
    assert len(form.errors) == numb_of_errors      


