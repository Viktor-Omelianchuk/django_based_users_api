=======================
Flask-based Weather app
=======================


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style
.. image:: https://travis-ci.org/Viktor-Omelianchuk/flask_based_weather_app.svg?branch=master&status=passed
    :target: https://travis-ci.org/Viktor-Omelianchuk/flask_based_weather_app.svg?branch=master
    :alt: Linux build status on Travis CI

:License: MIT

.. contents::

Website
-------------------

- http://flask-weather.eba-rqdaactq.us-west-2.elasticbeanstalk.com/


Installation
-------------------
On Unix, Linux, BSD, macOS, and Cygwin::

  $ git clone https://github.com/Viktor-Omelianchuk/flask_based_weather_app.git

Create and activate isolated Python environments
-------------------------------------------------
::

    $ cd flask_based_weather_app
    $ virtualenv env
    $ source env/bin/activate

Install requirements
--------------------------------------
::

    $ make install

Run local development server
--------------------------------------
::

    $ make run

Generate and view Sphinx HTML documentation
---------------------------------------------------------
::

    $ make docs

Run tests
-------------------
::

    $ make test


Check code coverage quickly with the default Python
---------------------------------------------------------
::

    $ make coverage

Remove all build, test, coverage and Python artifacts
---------------------------------------------------------
::

    $ make clean

Build docker image
-------------------
::

    $ docker build -t myimage .

Docker run
-------------------
::

    $ docker run --network host --name mycontainer -p 8000:8000 myimage


