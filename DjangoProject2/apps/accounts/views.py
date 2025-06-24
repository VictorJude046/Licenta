from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from .models import UserProfile

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.views.generic import TemplateView
    from django.shortcuts import render
    from .models import UserProfile

    class ProfileView(LoginRequiredMixin, TemplateView):
        template_name = "accounts/profile.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = self.request.user
            profile = getattr(user, 'userprofile', None)

            context['user'] = user
            context['profile'] = profile
            return context


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")
