# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from events.event import Event


def _setup_events(conf):
    """Setup the events defined in the settings."""
    events = {}
    for name in conf.keys():
        events[name] = Event(name=name)
        for listener in conf[name]:
            action = 'run'
            if ':' in listener:
                listener, action = listener.rsplit(':')
            events[name].add_listener(listener, action)

    # Add events to module scope.
    globals().update(events)


_setup_events(getattr(settings, 'EVENTS', {}))
