# -*- coding: utf-8 -*-


class Event(object):
    """Class to reperesent an event."""

    def __init__(self, name):
        self.name = name
        self._listeners = []

    def add_listener(self, l):
        self._listeners.append(l)

    def emit(self, *args, **kwargs):
        for l in self._listeners:
            try:
                l()(*args, **kwargs)
            except Exception:
                pass
