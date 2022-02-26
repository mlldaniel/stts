from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    comment = models.TextField(default='', blank=True)
