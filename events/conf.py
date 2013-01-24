# -*- coding: utf-8 -*-

from django.conf import settings                            # NOQA
from appconf import AppConf


class EventsConf(AppConf):
    STORE_OBJECT = "django.core.cache.cache"
