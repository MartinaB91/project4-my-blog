from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    This class is used for controlling what the Admin can see,
    filter, edit and search for in admin profile list
    """
    model = Profile

    list_display = (
        'user',
        'first_name',
        'last_name',
        'profile_email',
    )

    list_filter = (
        'user',
        'first_name',
        'last_name',
    )

    list_display_links = ('user',)

    search_fields = (
        'user',
        'first_name',
        'last_name',
    )

