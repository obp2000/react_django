from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from .forms import LoginForm, RegisterForm, UserPasswordChangeForm


class UserAPIView(RetrieveAPIView):
    """
    API endpoint that allows get user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(GenericAPIView):
    """
    API endpoint that allows register user.
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPIView(GenericAPIView):
    """
    API endpoint that allows user to login.
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


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
