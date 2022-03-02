apps.speech\_results package
============================

- All related to speech to text function is handled here
    - Make result(service.py)
    - Store result
    - Fetch Results

Subpackages
-----------

.. toctree::
   :maxdepth: 1

   apps.speech_results.migrations

DB migrations files

Submodules
----------

apps.speech\_results.admin module
---------------------------------

.. automodule:: apps.speech_results.admin
   :members:
   :undoc-members:
   :show-inheritance:


Admin page setting


apps.speech\_results.apps module
--------------------------------

.. automodule:: apps.speech_results.apps
   :members:
   :undoc-members:
   :show-inheritance:

Config file for current app


apps.speech\_results.forms module
---------------------------------

.. automodule:: apps.speech_results.forms
   :members:
   :undoc-members:
   :show-inheritance:

Contain form when user request for speech to text conversion.
(CreateSpeechResultsForm)

apps.speech\_results.models module
----------------------------------

.. automodule:: apps.speech_results.models
   :members:
   :undoc-members:
   :show-inheritance:

Model to store "speech to text" results:

ApiResult in SpeechResults isn't actual model, its here to reference 'result' field's format since it is in JsonField.
Basically it stores, request user, original filename and the result of the request from the google cloud api.

.. code-block:: Python

    class SpeechResults(models.Model):
        # format of result JSONField
        class ApiResult:
            def __init__(self, transcript='', language_code='', result_end_time=''):
                self.transcript = transcript
                self.language_code = language_code
                self.result_end_time = result_end_time

        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
        org_filename = models.TextField(verbose_name='Original File name')

        # ApiResult format
        result = JSONField(verbose_name='Result from Speech Api')

        created_at = models.DateTimeField(verbose_name='Created DateTime', auto_now_add=True)
        updated_at = models.DateTimeField(verbose_name='Updated DateTime', auto_now=True)

        class Meta:
            verbose_name = verbose_name_plural = 'Result of Speech to text from speech recognition api'

apps.speech\_results.services module
------------------------------------

.. automodule:: apps.speech_results.services
   :members:
   :undoc-members:
   :show-inheritance:



Logic for 'speech to text' conversion.

process_speech_to_text function is been called from the view.
There are 4 steps divided into 4 functions. In Each step error could happens ,
when it does it raise Custom Error from config.errors and return the message to the render them into the form.

.. code-block:: python

    def process_speech_to_text(mp4_in_mem) # receive file located in memory

    def _temp_save_mp4(mp4_in_mem) # temporarily save the mp4 file
    def _convert_mp4_to_wav(org_file) # convert the temporarily saved the mp4 file to wav
    def _get_audio_length(file) # get audio length
    def _request_for_speech_to_text(content) # request for speech conversion


apps.speech\_results.tests module
---------------------------------

.. automodule:: apps.speech_results.tests
   :members:
   :undoc-members:
   :show-inheritance:

Currently not used


apps.speech\_results.views module
---------------------------------

.. automodule:: apps.speech_results.views
   :members:
   :undoc-members:
   :show-inheritance:


There are 2 views to handle
- speech to text conversion : CreateSpeechResultsView
- view speech to text results: ListSpeechResultsView
