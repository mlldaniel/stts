from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import SpeechResultSerializer
from apps.speech_results.models import SpeechResults


class SpeechResultViewSet(ModelViewSet):
    queryset = SpeechResults.objects.all()
    serializer_class = SpeechResultSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    # match filter
    filterset_fields = ['org_filename', 'user__username']
    # ordering
    ordering_fields = ['id', 'created_at', 'user']
    ordering = ['-id']

    search_fields = ['org_filename', 'result']

    http_method_names = ['get', 'options']
