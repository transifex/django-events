# -*- coding: utf-8 -*-

"""
Base classes for possible actions taken on events.
"""

from events.conf import settings
from events.utils import import_object


class Action(object):
    """
    Base class of the hierarchy.

    The developer is expected to provide the necessary method(s) with
    the actual code to run.

    """

    def __init__(self, action):
        if action not in self._valid_actions:
            raise AttributeError("Action %s is not supported" % action)
        self.action = action
        mod_name, obj_name = settings.EVENTS_STORE_OBJECT.rsplit('.', 1)
        obj = import_object(mod_name, obj_name)
        if callable(obj):
            self._store = obj()
        else:
            self._store = obj

    def __call__(self, *args, **kwargs):
        if self.should_run(*args, **kwargs):
            return getattr(self, self.action)(*args, **kwargs)

    def should_run(self, *args, **kwargs):
        return True


class ImmediateAction(Action):
    """Action taken immediately."""


class CeleryAction(Action):
    """Background action through celery."""

    def __call__(self, *args, **kwargs):
        getattr(self, self.action).delay(*args, **kwargs)


class ConditionalActionMixin(object):
    """Take action only if a condition is met."""

    def __call__(self, *args, **kwargs):
        if self.should_run(*args, **kwargs):
            super(ConditionalActionMixin, self).__call__(*args, **kwargs)

    def should_run(self, *args, **kwargs):
        return True
