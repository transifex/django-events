## Events for django

Django events provides a simple mechanism for defining and responding to events
in django.

The mechanism is similar to signals and in some cases should replace them.


### Features

- Declarative definition of the events and their listeners in the settings. The
  developer defines all events and their listeners in the settings file and the
  app is responsible to expose them in the other apps.
- Base classes for actions that deal with the most common cases. Specifically:

    - Responding to events with a plain function.
    - Responding to events in a celery task.
    - Responding to events, only if a condition is met.
    - Responding to events, only when the event signals a *status change*.

- Easier testing; the developer can remove all listeners for the events, when
  running the tests.


### Status-change listeners

There are cases where certain things in an application have status, e.g. tests
passing or not. In such cases you might want to notify the users, only when the
status changes, i.e. going from "tests passing" to "tests failing" and the other
way round.

The `EdgeTriggeredAction` class provides this feature.


### Usage

First, add the app in the `INSTALLED_APPS` and define the events and their
listeners in the settings file:

    INSTALLED_APPS += ['events']

    EVENTS = {
        'tests_pass': [
            'myapp.actions.Action1',
            'myapp.actions.Action2',
        ]
    }

Then, in the place you want to emit the event, do:

    from events.models import tests_pass

    tests_pass.emit(args)


In the `myapp.actions` module define the two actions:

    from events.actions import Action

    class Action1(Action):
        pass


    class Action2(Action):
        pass
