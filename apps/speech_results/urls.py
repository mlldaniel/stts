from django.urls import path
from . import views

app_name = "speech_results"
urlpatterns = [
    path('create', views.CreateSpeechResultsView.as_view(), name="create"),
    path('', views.ListSpeechResultsView.as_view(), name="list"),
    # TODO view detail page
    # path('<int:pk>', views.DetailSpeechResultsView.as_view(), name="detail"),

]
