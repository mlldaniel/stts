from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.username = username
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    # TODO allow user to get the result if he/she is confirmed
    confirmed = models.BooleanField(verbose_name='Whether user can use the service', default=False)
    comment = models.TextField(verbose_name='Comment', default='', blank=True)

    objects = CustomUserManager()
