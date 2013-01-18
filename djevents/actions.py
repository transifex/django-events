# -*- coding: utf-8 -*-

"""
Base classes for possible actions taken on events.
"""


class Action(object):
    """
    Base class of the hierarchy.

    The developer is expected to provide the run method with the actual
    code to run.

    """

    def run(self, *args, **kwargs):
        return

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)


class ImmediateAction(Action):
    """Action taken immediately."""


class CeleryAction(Action):
    """Background action through celery."""

    def __call__(self, *args, **kwargs):
        self.run.delay(*args, **kwargs)


class ConditionalActionMixin(object):
    """Take action only if a condition is met."""

    def __call__(self, *args, **kwargs):
        if self.should_run(*args, **kwargs):
            super(ConditionalActionMixin, self).__call__(*args, **kwargs)

    def should_run(self, *args, **kwargs):
        return True
