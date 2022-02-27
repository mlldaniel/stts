
avconv -i sample.mp4 -ac 1 -vn -f wav sample.wav

=====
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"



export GOOGLE_APPLICATION_CREDENTIALS="/Users/gyedan/PycharmProjects/favorite_medium/speech-to-text/env/fm-stts-daeef083dcea.json"

f = open("/Users/gyedan/PycharmProjects/favorite_medium/speech-to-text/tmp/sample.wav",'rb')

from apps.speech_results.service import request_for_speech_to_text

https://storage.cloud.google.com/stts-bucket/sample.wav

gs://stts-bucket/sample.wav
gs://stts-bucket/sample_2.wav

https://storage.cloud.google.com/cloud-samples-data/speech/brooklyn_bridge.raw
gs://cloud-samples-data/speech/brooklyn_bridge.raw

"/Users/gyedan/PycharmProjects/favorite_medium/speech-to-text/tmp/sample_2.wav"