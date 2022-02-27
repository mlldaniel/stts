# Imports the Google Cloud client library
import os
import subprocess
from pathlib import Path
import soundfile as sf
from tempfile import NamedTemporaryFile

from django import forms
from google.cloud import speech


def process_speech_to_text(mp4_in_mem):
    # store temp in tmp
    mp4_tmp_file = _temp_save_mp4(mp4_in_mem)
    dst_file_name = _convert_mp4_to_wav(mp4_tmp_file)
    if dst_file_name is None:
        return None

    seconds = _get_audio_length(dst_file_name)
    if seconds > 60:
        raise forms.ValidationError(f'mp4 audio length must be less than 1 minute. your result: {seconds}')

    results = []
    with open(dst_file_name, "rb") as wav_file:
        results = _request_for_speech_to_text_3(wav_file.read())

    return results


def _temp_save_mp4(mp4_in_mem):
    _, ext = os.path.splitext(mp4_in_mem.name)
    # with NamedTemporaryFile(prefix='upload_mp4-',suffix=ext) as tmp_mp4:
    mp4_tmp_file = NamedTemporaryFile(prefix='upload_mp4-', suffix=ext, delete=True)
    mp4_tmp_file.write(mp4_in_mem.read())
    mp4_tmp_file.flush()
    mp4_tmp_file.seek(0)
    return mp4_tmp_file


def _convert_mp4_to_wav(org_file):
    # org_file_name = os.path.basename(org_file.name)
    # dst_path = os.path.dirname(org_file.name)
    # dst_file = os.path.join(dst_path,f'{org_file_name}')
    org_file_name = Path(org_file.name)
    dst_file_name = org_file_name.with_suffix('.wav')
    cmdline = ['avconv',
               '-i',
               org_file_name,
               '-ac',
               ' 1',
               '-vn',
               '-f',
               'wav',
               dst_file_name]
    try:
        subprocess.call(cmdline)
    except OSError:
        return None

    return dst_file_name


def _get_audio_length(file) -> float:
    f = sf.SoundFile(file)
    print('samples = {}'.format(f.frames))
    print('sample rate = {}'.format(f.samplerate))
    print('seconds = {}'.format(f.frames / f.samplerate))
    seconds = f.frames / f.samplerate
    return seconds


def request_for_speech_to_text(file_content: bytes):
    # outsite .env
    print(os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS',
                                '/Users/gyedan/PycharmProjects/favorite_medium/speech-to-text/env/fm-stts-daeef083dcea.json'))
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    # gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

    # audio = speech.RecognitionAudio(uri=gcs_uri)
    audio = speech.RecognitionAudio(content=file_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))


def request_for_speech_to_text_2(uri):
    # outsite .env
    print(os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS',
                                '/Users/gyedan/PycharmProjects/favorite_medium/speech-to-text/env/fm-stts-daeef083dcea.json'))
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    # gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

    # audio = speech.RecognitionAudio(uri=gcs_uri)
    audio = speech.RecognitionAudio(uri=uri)
    # audio = speech.LongRunningRecognize(uri=uri)

    config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))


def local_audio_to_text(path):
    f = open(path, "rb")

    # request_for_speech_to_text_3(f.read())


def _request_for_speech_to_text_3(content):
    # outsite .env
    print(os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS',
                                '/Users/gyedan/PycharmProjects/favorite_medium/speech-to-text/env/fm-stts-daeef083dcea.json'))
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

    results = []
    for result in response.results:
        try:
            # json format in model
            results.append({
                "transcript": result.alternatives[0].transcript,
                "language_code": result.language_code,
                "result_end_time": str(result.result_end_time),
            })
        except:
            continue
        print("Transcript: {}".format(result.alternatives[0].transcript))

    return results
