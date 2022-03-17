from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView)
from django.contrib.messages.views import SuccessMessageMixin
# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
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
    model = get_user_model()
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


class UserDetail(LoginRequiredMixin, DetailView):
    template_name = 'user_auth/detail.html'
    login_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user
