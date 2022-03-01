from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import SpeechResultSerializer
from apps.speech_results.models import SpeechResults


class SpeechResultViewSet(ModelViewSet):
    queryset = SpeechResults.objects.all()
    serializer_class = SpeechResultSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, OrderingFilter)

    filterset_fields = ['org_filename', 'user__username']

    ordering_fields = ['id']
    ordering = ['-id']

    http_method_names = ['get', 'options']
