.. Speech To Text documentation master file, created by
   sphinx-quickstart on Tue Mar  1 22:06:35 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Speech To Text's documentation!
==========================================


Introduction
------------
This project is for Favorite Medium coding test. It allow user to upload
mp4 file and transform the audio to text.

-  App name: Speech To Text
-  This project has Web and API.

================== ============================================
Name               Description
================== ============================================
Language           Python 3.9
UI/CSS             HTML/Tailwind
Framework          Django 3.1.14 / Django Rest Framework 3.13.1
Speech to Text api Cloud Speech-to-Text - Google CLoud
================== ============================================

Main features
-------------

-  Separated dev and production settings(heroku)

-  Request for Transform mp4 to text

-  View Results in Web/Api

-  User registration and logging/logout

-  Procfile for easy deployments

-  Separated requirements files


Basic project structure
-----------------------
.. code-block:: bash

   .
   ├── README.md            # Basic information and instructions to install&run
   ├── Aptfile              # heroku: installation files
   ├── Procfile             # heroku: allow to run gunicorn
   ├── bin                  # heroku: where extra binary program will be installed(avconv)
   ├── vendor               # heroku: temporarily download folder for avconv program
   ├── runtime.txt          # heroku: required to run on correct version of python
   ├── api                  # Django: rest framework api apps
   ├── apps                 # Django: web apps
   ├── config               # Django: common django config folder including settings
   ├── manage.py            # Django: command-line utility for administrative tasks
   ├── static               # Django: static files
   ├── static_root          # Django: static files when manage.py collectstatic
   ├── templates            # Django: all web app templates
   ├── docs                 # Current documentations folder
   ├── requirements.txt     # Python: required python packages to run the server
   └── venv                 # Python: not include in git but good to store your virtualenv here


Indices and tables
==================

* :ref:`search`

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules.rst
   usage.rst


