from django.contrib import admin
from . import models


@admin.register(models.SpeechResults)
class SpeechResultsAdmin(admin.ModelAdmin):
    pass
