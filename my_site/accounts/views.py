from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class LogoutView(BaseLogoutView):
    """TODO: Maybe I could use the LoginRequiredMixin here."""
    template_name = 'accounts/logout.html'


def index(request):
    return HttpResponse('This is the profile page.')


def register(request):
    return HttpResponse('This is the register page.')
