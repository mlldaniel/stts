api.speech\_results package
===========================

Basic structure


.. code-block:: bash

    .
    ├── serializers.py
    ├── urls.py
    └── views.py


-  Views are based on ModelViewSet
    - 3 types of filter used = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    - Authenticated user only
-  Serializer are based on ModelSerializer
-  No model here, Views/Serializer is using model from apps.speech_results.model

