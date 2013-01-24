# -*- coding: utf-8 -*-

import importlib


def import_object(module_name, object_name):
    """
    Import object_name from module_name.

    Import the object `object_name` from the module `module_name`.

    The `module_name` should be a fully qualified path.

    """
    return getattr(importlib.import_module(module_name), object_name)
