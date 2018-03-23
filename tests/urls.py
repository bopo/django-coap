# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_coap.urls import urlpatterns as django_coap_urls

urlpatterns = [
    url(r'^', include(django_coap_urls, namespace='django_coap')),
]
