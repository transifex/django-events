# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging

from events.utils import import_object


class Event(object):
    """Class to reperesent an event."""

    def __init__(self, name):
        self.name = name
        self._listeners = []
        self._actions = None

    def add_listener(self, listener, action):
        """Add a listener with an action.

        :param listener: An class object that supports Action interface,
                         or a string that describes from where to import this class.
        :param action: The name the Action's method to call.
        """
        self._listeners.append((listener, action))
        self._actions = None  # invalidate action cache

    def clear_listeners(self):
        self._listeners = []
        self._actions = None

    @property
    def actions(self):
        if self._actions is None:
            self._actions = []
            for listener, action in self._listeners:
                try:
                    mod_name, obj_name = listener.rsplit('.', 1)
                except AttributeError:
                    klass = listener
                else:
                    klass = import_object(mod_name, obj_name)
                self._actions.append((action, klass))
        return self._actions

    def emit(self, *args, **kwargs):
        logger = logging.getLogger('events')
        for name, klass in self.actions:
            try:
                callable = klass(action=name)
            except Exception:
                logger.exception(
                    "Error instantiating action %s for event %s",
                    name, self.name)
            else:
                try:
                    callable(*args, **kwargs)
                except Exception:
                    logger.exception(
                        "Error emitting %s (%s)", self.name, name)
