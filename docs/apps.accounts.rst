apps.accounts package
=====================

- Inherit default AbstractUser
- Manage user model(name account)


Subpackages
-----------

.. toctree::
   :maxdepth: 1

   apps.accounts.migrations.rst

DB migrations files

apps.accounts.admin module
--------------------------

.. automodule:: apps.accounts.admin
   :members:
   :undoc-members:
   :show-inheritance:

Admin page setting

apps.accounts.apps module
-------------------------

.. automodule:: apps.accounts.apps
   :members:
   :undoc-members:
   :show-inheritance:

Config file for current app

apps.accounts.forms module
--------------------------

.. automodule:: apps.accounts.forms
   :members:
   :undoc-members:
   :show-inheritance:

Form related to account(user) model currently there is only on form RegisterForm, which is used to register

apps.accounts.mixins module
---------------------------

.. automodule:: apps.accounts.mixins
   :members:
   :undoc-members:
   :show-inheritance:


Mixin for views to check Logged in user or logged out user
- LoggedOutOnlyView
- LoggedInOnlyView



apps.accounts.models module
---------------------------

.. automodule:: apps.accounts.models
   :members:
   :undoc-members:
   :show-inheritance:

User account model reside here


apps.accounts.urls module
-------------------------

.. automodule:: apps.accounts.urls
   :members:
   :undoc-members:
   :show-inheritance:

urls file

apps.accounts.views module
--------------------------

.. automodule:: apps.accounts.views
   :members:
   :undoc-members:
   :show-inheritance:

View to Register, for login or logout views django.contrib.auth is used.

Module contents
---------------

.. automodule:: apps.accounts
   :members:
   :undoc-members:
   :show-inheritance:
