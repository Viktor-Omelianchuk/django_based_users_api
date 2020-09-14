=======================
Django_based_users_api
=======================


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

.. contents::

Installation
-------------------
On Unix, Linux, BSD, macOS, and Cygwin::

  $ git clone https://github.com/Viktor-Omelianchuk/django_based_users_api.git

Create and activate isolated Python environments
-------------------------------------------------
::

    $ cd django_based_users_api
    $ virtualenv env
    $ source env/bin/activate

Install requirements
--------------------------------------
::

    $ make install

Migrations
--------------------------------------
::

    $ make makemigrations
    $ make migrate


Create superuser
--------------------------------------
::

    $ make createsuperuser


Run local development server
--------------------------------------
::

    $ make run


Run tests
---------------------------------------------------------
::

    $ make test

Available endpoints
--------------------


User registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

     Endpoint: /api/user/registration/
     Method: POST
 
Data of all users
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

     Endpoint: /api/user/all_users/
     Method: GET

User data
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

     Endpoint: /api/user/{id}/
     Method: GET, PUT, DELETE
     GET - available to all authenticated users
     PUT, DELETE - available to either owner or administrator
     
    
GET Token
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

     Endpoint: /api/token-auth/
     Method: POST
     username and password are required
     
GET Token with browser UI
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

     Endpoint: /api/auth_token/token/login
     Method: POST
     username and password are required

Change password
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

     Endpoint: /api/change-password/
     Method: PUT
     Password change requires authentication and old password
     
Reset password
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

     Endpoint: /api/password_reset/
     Method: POST
     After specifying "email" a one-time token for password reset will be sent to email
     (temporarily the token is output to the console)
     
Password reset confirmation
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

     Endpoint: /api/password_reset/confirm/
     Method: POST
     Need a one-time token from the email and a new password

