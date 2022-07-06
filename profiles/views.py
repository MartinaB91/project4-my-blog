from django.shortcuts import render
from .models import Profile
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SettingsForm
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class SettingsView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    """
    Used for showing settings page
    """

    model = Profile
    form_class = SettingsForm
    template_name = "user_settings.html"

    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        user = self.request.user.profile
        context["SettingsForm"] = Profile(
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "profile_img": user.profile_img,
            }
        )

        return context

    def get_success_url(self):
        messages.success(self.request, "You settings has been updated successfully!")
        return reverse_lazy("settings", kwargs={"pk": self.object.id})
