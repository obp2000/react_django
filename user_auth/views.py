from django.contrib.auth.models import User
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView)
from django.contrib.messages.views import SuccessMessageMixin
# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView

from .forms import LoginForm, RegisterForm, UserPasswordChangeForm


class UserLoginView(SuccessMessageMixin, LoginView):
    authentication_form = LoginForm
    template_name = 'user_auth/login.html'
    success_message = _("successfully").title()


class UserLogoutView(SuccessMessageMixin, LogoutView):
    template_name = 'user_auth/logged_out.html'
    success_message = _("successfully").title()


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'user_auth/register.html'
    success_message = _("successfully").title()
    success_url = reverse_lazy('customer-list')


class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'user_auth/password_change_form.html'
    success_message = _("successfully").title()


class UserPasswordChangeDoneView(SuccessMessageMixin, PasswordChangeDoneView):
    template_name = 'user_auth/password_change_done.html'
    success_message = _("successfully").title()


# def register1(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()

#         return redirect("/home")
#     else:
#         form = RegisterForm()
#     return render(request, "register/register.html",
#                   {"form": form})
