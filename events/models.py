import importlib
from django.conf import settings
from events.event import Event


# Django automatically executes the models module of each
# installed app, so we read the settings here to ensure proper
# initialization, without messing with the settings.

def _setup_events(conf):
    """Setup the events defined in the settings."""
    events = {}
    event_names = conf.keys()
    for name in event_names:
        events[name] = Event(name=name)
        for listener in conf[name]:
            action = 'run'
            if ':' in listener:
                listener, action = listener.rsplit(':')
            mod_name, obj_name = listener.rsplit('.', 1)
            klass = getattr(importlib.import_module(mod_name), obj_name)
            events[name].add_listener(klass, action)

    # Add events to module scope.
    globals().update(events)


_setup_events(getattr(settings, 'EVENTS', {}))
