from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from .forms import LoginForm, ProfileForm


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


def register(request):
    return HttpResponse('This is the register page.')
