# Introduction

This project is for Favorite Medium coding test. It allow user to upload mp4 file and transform the audio to text.

- App name: Speech To Text
- This project has Web and API.

| Name                 | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| Language             | Python 3.9                                                        |
| UI/CSS               | HTML/Tailwind                                                     |
| Framework            | Django 3.1.14 / Django Rest Framework 3.13.1                      |
| Speech to Text api   | Cloud Speech-to-Text - Google CLoud                               |

### Main features

* Separated dev and production settings(heroku)

* Request for Transform mp4 to text

* View Results in Web/Api

* User registration and logging/logout

* Procfile for easy deployments

* Separated requirements files

# 1. Local Execution

## Installation

First you have to install virtualenv based on python 3.9

If your project is already in an existing python3 virtualenv first activate the environment and install all packages

    $ pip install -r requirements.txt

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Prepare for GOOGLE_APPLICATION_CREDENTIALS from https://cloud.google.com/speech-to-text/docs/before-you-begin and
download it somewhere safe

Prepare for a Postgresql database

## Config file

First, you need to create .env in the root of the project folder

    $ touch .env

Fill the following values

    DEBUG=True
    #Django SECRET_KEY
    SECRET_KEY= 
    GOOGLE_APPLICATION_CREDENTIALS_PATH= {Path to certificat.json}
    DATABASE_NAME=
    DATABASE_USER=
    DATABASE_PASS=
    DATABASE_HOST=

## Run

Finally, you need to run migrations command and run the server. (virtual environment must be activated)

Migrations:

    $ python manage.py migrate --settings=config.settings.local

Run the development server:

    $ python manage.py runserver --settings=config.settings.local
    $ python manage.py createsuperuser --settings=config.settings.local

# 2. Heroku Execution

Create Postgresql Database It will automatically set DATABASE_URL

Add Config Vars

- DATABASE_URL
- DEBUG=True
- DJANGO_SETTINGS_MODULE=config.settings.heroku
- GOOGLE_APPLICATION_CREDENTIALS=google-credentials.json
- GOOGLE_APPLICATION_CREDENTIALS_PATH=google-credentials.json
- GOOGLE_CREDENTIALS={google credential}
- SECRET_KEY={secret key for django}

Add Build Packs

- heroku/python
- https://github.com/buyersight/heroku-google-application-credentials-buildpack
- https://github.com/heroku/heroku-buildpack-apt
- https://github.com/MarmosetMusic/avconv-buildpack

Change Allowed host to heroku generated one

Run migrations with heroku config

    $ python manage.py runserver --settings=config.settings.heroku
    $ python manage.py createsuperuser --settings=config.settings.heroku

# Documentation

Documentation file reside in /docs

To view them in html site. run the following command in /docs path

    $ cd docs
    $ make html

Open /docs/_build/index.html to view them
