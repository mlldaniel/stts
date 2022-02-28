from django.db import models
from django.db.models import JSONField
from config.settings import base as settings


class SpeechResults(models.Model):
    # format of result JSONField
    class ApiResult:
        def __init__(self, transcript='', language_code='', result_end_time=''):
            self.transcript = transcript
            self.language_code = language_code
            self.result_end_time = result_end_time

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    org_filename = models.TextField(verbose_name='Original File name')

    # ApiResult format
    result = JSONField(verbose_name='Result from Speech Api')

    created_at = models.DateTimeField(verbose_name='Created DateTime', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated DateTime', auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Result of Speech to text from speech recognition api'


