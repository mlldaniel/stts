import os

from django import forms
from django.core.exceptions import ValidationError


class CreateSpeechResultsForm(forms.Form):
    # validate if it is audio

    audio_file = forms.FileField()

    def get_cleaned_data(self, *args, **kwargs):
        # valid_file_extensions = [".mp4", ".mp3",".wav"]
        valid_file_extensions = [".mp4", ]
        try:
            audio_file = self.cleaned_data.get('audio_file')
            _, ext = os.path.splitext(audio_file.name)
            if ext.lower() not in valid_file_extensions:
                raise ValidationError("Unacceptable file extension.")
        except Exception as ex:
            raise ValidationError("Unacceptable file extension.")

        return audio_file
