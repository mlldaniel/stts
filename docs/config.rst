config package
==============

Basically config package is django base package generated when creating project with django command.

Subpackages
-----------

.. toctree::
   :maxdepth: 4

   config.settings

Submodules
----------

config.asgi module
------------------

.. automodule:: config.asgi
   :members:
   :undoc-members:
   :show-inheritance:

ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/


config.errors module
--------------------

.. automodule:: config.errors
   :members:
   :undoc-members:
   :show-inheritance:

Custom Error that are use when Exception Handling.
Currently, it is mainly used during speech to text proccess (apps.speech_results.service.py)


config.urls module
------------------

.. automodule:: config.urls
   :members:
   :undoc-members:
   :show-inheritance:

Base urls file, all urls from api/apps are connected here


config.wsgi module
------------------

.. automodule:: config.wsgi
   :members:
   :undoc-members:
   :show-inheritance:

WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/



.. automodule:: config
   :members:
   :undoc-members:
   :show-inheritance:
