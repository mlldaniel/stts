from django.urls import path
from . import views

app_name = "speech_results"
urlpatterns = [
    path('new', views.CreateSpeechResultsView.as_view(), name="speech_results_create")
]
