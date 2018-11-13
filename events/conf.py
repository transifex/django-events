# -*- coding: utf-8 -*-

"""
Configuration variables; gets them from django settings, falls back to a
default
"""

from __future__ import unicode_literals

from django.conf import settings

DEFAULT_STORE_OBJECT = "django.core.cache.cache"
EVENTS_STORE_OBJECT = getattr(settings, 'EVENTS_STORE_OBJECT',
                              DEFAULT_STORE_OBJECT)
