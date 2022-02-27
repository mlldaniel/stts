from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView
from . import services

from .forms import CreateSpeechResultsForm
from .models import SpeechResults


class CreateSpeechResultsView(FormView):
    form_class = CreateSpeechResultsForm
    template_name = 'speech_results/speech_results_create.html'

    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # InMemoryUploadedFile type
        mp4_in_mem = form.get_cleaned_data()
        result = services.process_speech_to_text(mp4_in_mem)

        # todo change to autheticated user
        saved_result = SpeechResults.objects.create(user_id=1, org_filename=mp4_in_mem.name, result=result)

        # services.sound_file_size(file)
        # TODO exception handling
        # file_content = file.read()
        # service.request_for_speech_to_text(file_content)
        # org_filename = file

        return redirect(reverse("core:home"))
