=====
Usage
=====

To use django-coap in a project, add it to your `INSTALLED_APPS`:

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
