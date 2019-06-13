# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from setuptools import setup

setup(
    name="django-events",
    version="0.3.1",
    description="Events in django applications.",
    author="Apostolis Bessas",
    author_email="mpessas@transifex.com",
    packages=["events"],
    install_requires=["Django"],
)
