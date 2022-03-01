from rest_framework import serializers

from apps.speech_results.models import SpeechResults


class SpeechResultSerializer(serializers.ModelSerializer):
    """ContractComment 계약서 댓글"""

    class Meta:
        verbose_name = verbose_name_plural = "Speech To Text Result"
        model = SpeechResults
        fields = "__all__"
