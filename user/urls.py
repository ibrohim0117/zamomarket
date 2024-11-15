from django.contrib import admin
from django.urls import path
from user.views import (
    UserRegistrationAPIView, VerifyUserAPIView,
    UserLoginView
)

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='signup'),
    path('code/', VerifyUserAPIView.as_view(), name='code'),
    path('login/', UserLoginView.as_view(), name='signin'),
]
