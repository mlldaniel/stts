from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView

from config.errors import RecognitionAudioRequestError, AudioLengthIrretrievableError, ConvertAudioToWavError, \
    TemporarySaveAudioError
from . import services

from .forms import CreateSpeechResultsForm
from .models import SpeechResults
from ..accounts.mixins import LoggedInOnlyView


class CreateSpeechResultsView(LoggedInOnlyView, FormView):
    form_class = CreateSpeechResultsForm
    template_name = 'speech_results/speech_results_create.html'
    success_url = reverse_lazy("speech_results:list")

    def form_valid(self, form):
        if not self.request.user.confirmed:
            return HttpResponseRedirect(reverse("core:home"))

        try:
            mp4_in_mem = form.get_cleaned_data()
            result = services.process_speech_to_text(mp4_in_mem)
        except ValidationError as err:
            form.custom_errors = str(err)
            return super().form_invalid(form)
        except TemporarySaveAudioError as err:
            form.custom_errors = f"Temporarily Saving Audio Error: {err}"
            return super().form_invalid(form)
        except ConvertAudioToWavError as err:
            form.custom_errors = f"Converting Audio To Wave Error: {err}"
            return super().form_invalid(form)
        except AudioLengthIrretrievableError as err:
            form.custom_errors = f"Could not get audio Length: {err}"
            return super().form_invalid(form)
        except RecognitionAudioRequestError as err:
            form.custom_errors = f"Could not convert to text: {err}"
            return super().form_invalid(form)

        try:
            SpeechResults.objects.create(user_id=self.request.user.id, org_filename=mp4_in_mem.name, result=result)
        except Exception as ex:
            form.custom_errors = f"Could not save the result: {ex}"
            return super().form_invalid(form)

        return super().form_valid(form)


class ListSpeechResultsView(LoggedInOnlyView, ListView):
    queryset = SpeechResults.objects.all()
    model = SpeechResults
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "results"
    template_name = 'speech_results/speech_results_list.html'

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)


class DetailSpeechResultsView(LoggedInOnlyView, DetailView):
    model = SpeechResults
    template_name = 'speech_results/speech_results_detail.html'
