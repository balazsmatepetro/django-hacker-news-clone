from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _

from .forms import LoginForm, ProfileForm, RegisterForm
from .models import User


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class LogoutView(BaseLogoutView):
    """TODO: Maybe I could use the LoginRequiredMixin here."""
    template_name = 'accounts/logout.html'


@login_required
def index(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            messages.success(request, _('You\'ve successfully updated your profile!'))

            return redirect('accounts:index')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'accounts/index.html', {
        'form': form,
    })


@user_passes_test(test_func=lambda user: not user.is_authenticated, redirect_field_name='')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, _('You\'ve successfully registered! Feel free to login with your credentials!'))

            return redirect('accounts:login')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form,
    })


def details(request, username: str):
    user_data = get_object_or_404(User, username=username)

    return render(request, 'accounts/details.html', {
        'user_data': user_data,
    })
