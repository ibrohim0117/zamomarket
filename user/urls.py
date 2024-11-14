from django.contrib import admin
from django.urls import path
from user.views import UserRegistrationAPIView

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='signup'),
]
