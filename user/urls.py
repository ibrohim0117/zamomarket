from django.contrib import admin
from django.urls import path
from user.views import (
    UserRegistrationAPIView, VerifyUserAPIView,
    UserLoginView, UserProfileView
)

urlpatterns = [
    # auth
    path('signup/', UserRegistrationAPIView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='signin'),
    path('code/', VerifyUserAPIView.as_view(), name='code'),

    # profile
    path('get-me/', UserProfileView.as_view(), name='get_me'),
]
