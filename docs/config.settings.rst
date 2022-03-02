config.settings package
=======================

Basic structure


.. code-block:: bash

    .
    ├── base.py
    ├── heroku.py
    └── local.py


Django settings files are here, currently there is 3 files.

Currently, local and heroku execution are supported, the base.py is the setting files included in both execution methods.


config.settings.base module
---------------------------

.. automodule:: config.settings.base
   :members:
   :undoc-members:
   :show-inheritance:

It includes most of the django settings such as ALLOWED_HOSTS, INSTALLED_APPS, MIDDLEWARE, TEMPLATES ...etc
Except DATABASES setting which is specifically set in heroku or local.


config.settings.heroku module
-----------------------------

.. automodule:: config.settings.heroku
   :members:
   :undoc-members:
   :show-inheritance:

Used when deploying to heroku. It includes base.py and heroku DB setting.

config.settings.local module
----------------------------

.. automodule:: config.settings.local
   :members:
   :undoc-members:
   :show-inheritance:

Used when deploying locally. It includes base.py and local DB setting.


.. automodule:: config.settings
   :members:
   :undoc-members:
   :show-inheritance:
