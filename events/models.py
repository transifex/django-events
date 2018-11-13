# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from events.event import Event
from events.utils import import_object


def _setup_events(conf):
    """Setup the events defined in the settings."""
    events = {}
    for name in conf.keys():
        events[name] = Event(name=name)
        for listener in conf[name]:
            action = 'run'
            if ':' in listener:
                listener, action = listener.rsplit(':')
            mod_name, obj_name = listener.rsplit('.', 1)
            klass = import_object(mod_name, obj_name)
            events[name].add_listener(klass, action)

    # Add events to module scope.
    globals().update(events)


_setup_events(getattr(settings, 'EVENTS', {}))
