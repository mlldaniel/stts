# Imports the Google Cloud client library
import os
import subprocess
from pathlib import Path
import soundfile as sf
from tempfile import NamedTemporaryFile
from apps.speech_results.models import SpeechResults

from django import forms
from google.cloud import speech

from config.errors import TemporarySaveAudioError, ConvertAudioToWavError, AudioLengthIrretrievableError, \
    RecognitionAudioRequestError


def process_speech_to_text(mp4_in_mem):
    # store temp in tmp
    mp4_tmp_file = _temp_save_mp4(mp4_in_mem)
    dst_file_name = _convert_mp4_to_wav(mp4_tmp_file)
    if dst_file_name is None:
        return None

    seconds = _get_audio_length(dst_file_name)
    if seconds > 60:
        formatted_seconds = "{0:.2f}".format(seconds)
        raise forms.ValidationError(f'mp4 audio length must be less than 1 minute. your result: {formatted_seconds}')

    results = []
    with open(dst_file_name, "rb") as wav_file:
        results = _request_for_speech_to_text(wav_file.read())

    return results


def _temp_save_mp4(mp4_in_mem):
    try:
        _, ext = os.path.splitext(mp4_in_mem.name)
        # with NamedTemporaryFile(prefix='upload_mp4-',suffix=ext) as tmp_mp4:
        mp4_tmp_file = NamedTemporaryFile(prefix='upload_mp4-', suffix=ext, delete=True)
        mp4_tmp_file.write(mp4_in_mem.read())
        mp4_tmp_file.flush()
        mp4_tmp_file.seek(0)
    except Exception as ex:
        raise TemporarySaveAudioError(ex)
    return mp4_tmp_file


def _convert_mp4_to_wav(org_file):
    try:
        org_file_name = Path(org_file.name)
        dst_file_name = org_file_name.with_suffix('.wav')

        cmdline = ['pwd',]
        subprocess.call(cmdline)

        cmdline = ['bin/avconv',
                   '-i',
                   org_file_name,
                   '-ac',
                   ' 1',
                   '-vn',
                   '-f',
                   'wav',
                   dst_file_name]

        subprocess.call(cmdline)
    except OSError as err:
        raise ConvertAudioToWavError(err)

    return dst_file_name


def _get_audio_length(file) -> float:
    try:
        f = sf.SoundFile(file)
        print('samples = {}'.format(f.frames))
        print('sample rate = {}'.format(f.samplerate))
        print('seconds = {}'.format(f.frames / f.samplerate))
        seconds = f.frames / f.samplerate
    except Exception as ex:
        raise AudioLengthIrretrievableError(ex)

    return seconds


def _request_for_speech_to_text(content):
    try:
        # Instantiates a client
        client = speech.SpeechClient()

        # The name of the audio file to transcribe
        audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            # sample_rate_hertz=16000,
            language_code="en-US",
        )

        # Detects speech in the audio file
        response = client.recognize(config=config, audio=audio)
    except Exception as ex:
        raise RecognitionAudioRequestError(ex)

    results = []
    for result in response.results:
        try:
            # json format in model
            results.append(SpeechResults.ApiResult(
                transcript=result.alternatives[0].transcript,
                language_code=result.language_code,
                result_end_time=str(result.result_end_time)).__dict__)
        except:
            continue

    return results
