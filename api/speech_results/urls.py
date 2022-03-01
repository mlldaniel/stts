from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SpeechResultViewSet

router = DefaultRouter()
router.register('speech_results', SpeechResultViewSet, basename="speech_results_api")
urlpatterns = [
    path('', include(router.urls)),
]
