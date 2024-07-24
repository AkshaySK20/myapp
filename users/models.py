from django.db import models
from django.contrib.auth.models import AbstractUser
from graphql_auth.models import UserStatus


class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name='email')

    #status = models.OneToOneField(UserStatus, on_delete=models.CASCADE, related_name="user", null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'