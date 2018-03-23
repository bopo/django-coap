=============================
django-coap
=============================

.. image:: https://badge.fury.io/py/django-coap.svg
    :target: https://badge.fury.io/py/django-coap

.. image:: https://travis-ci.org/bopo/django-coap.svg?branch=master
    :target: https://travis-ci.org/bopo/django-coap

.. image:: https://codecov.io/gh/bopo/django-coap/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/bopo/django-coap

Your project description goes here

Documentation
-------------

The full documentation is at https://django-coap.readthedocs.io.

Quickstart
----------

Install django-coap::

    pip install django-coap

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_coap.apps.DjangoCoapConfig',
        ...
    )

Add django-coap's URL patterns:

.. code-block:: python

    from django_coap import urls as django_coap_urls


    urlpatterns = [
        ...
        url(r'^', include(django_coap_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
