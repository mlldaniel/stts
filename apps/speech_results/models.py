from django.db import models
from django.db.models import JSONField
from config.settings import base as settings


class SpeechResults(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    org_filename = models.TextField(verbose_name="Original File name")
    result = JSONField()

    created_at = models.DateTimeField(verbose_name='Created DateTime', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated DateTime', auto_now=True)
