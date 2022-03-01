from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import SpeechResultSerializer
from apps.speech_results.models import SpeechResults


class SpeechResultViewSet(ModelViewSet):
    queryset = SpeechResults.objects.all()
    serializer_class = SpeechResultSerializer
    permission_classes = (IsAuthenticated,)
    names = ['get', ]
