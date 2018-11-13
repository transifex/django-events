# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging


class Event(object):
    """Class to reperesent an event."""

    def __init__(self, name):
        self.name = name
        self._listeners = []

    def add_listener(self, l, action):
        self._listeners.append((l, action))

    def emit(self, *args, **kwargs):
        logger = logging.getLogger('events')
        for l, action in self._listeners:
            try:
                l(action=action)(*args, **kwargs)
            except Exception:
                logger.error("Error calling %s", action, exc_info=True)
