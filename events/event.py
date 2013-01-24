# -*- coding: utf-8 -*-


class Event(object):
    """Class to reperesent an event."""

    def __init__(self, name):
        self.name = name
        self._listeners = []

    def add_listener(self, l, action):
        self._listeners.append((l, action))

    def emit(self, *args, **kwargs):
        for l, action in self._listeners:
            try:
                l(action=action)(*args, **kwargs)
            except Exception:
                pass
