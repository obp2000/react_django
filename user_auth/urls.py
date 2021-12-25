# from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (UserLoginView, UserLogoutView, UserPasswordChangeDoneView,
                    UserPasswordChangeView, UserRegisterView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('password-change/',
         UserPasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/',
         UserPasswordChangeDoneView.as_view(),
         name='password_change_done')
]
