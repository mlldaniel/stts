from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    # TODO allow user to get the result if he/she is confirmed
    confirmed = models.BooleanField(verbose_name='Whether user can use the service', default=False)
    comment = models.TextField(verbose_name='Comment', default='', blank=True)
