import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class BaseCreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseCreatedModel):
    phone = models.CharField(max_length=25, unique=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def create_code(self):
        code = "".join([str(random.randint(1, 100) % 10) for _ in range(4)])
        UserConfirmation.objects.create(
            code=code,
            user_id=self.id
        )
        return code

    def token(self):
        refresh = RefreshToken.for_user(self)
        data = {
            "refresh_token": str(refresh),
            "access": str(refresh.access_token)
        }
        return data

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class UserConfirmation(BaseCreatedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='codes')
    code = models.CharField(max_length=4)
    expiration_time = models.DateTimeField(default=timezone.now() + timedelta(minutes=10))
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.code


