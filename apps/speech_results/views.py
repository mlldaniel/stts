from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView, ListView, DetailView
from . import services

from .forms import CreateSpeechResultsForm
from .models import SpeechResults


class CreateSpeechResultsView(FormView):
    form_class = CreateSpeechResultsForm
    template_name = 'speech_results/speech_results_create.html'

    success_url = "/"

    def form_valid(self, form):
        mp4_in_mem = form.get_cleaned_data()
        result = services.process_speech_to_text(mp4_in_mem)

        # todo change to autheticated user
        saved_result = SpeechResults.objects.create(user_id=1, org_filename=mp4_in_mem.name, result=result)

        return redirect(reverse("speech_results:list"))


class ListSpeechResultsView(ListView):
    queryset = SpeechResults.objects.all()
    model = SpeechResults
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "results"
    template_name = 'speech_results/speech_results_list.html'


class DetailSpeechResultsView(DetailView):
    model = SpeechResults
    template_name = 'speech_results/speech_results_detail.html'


