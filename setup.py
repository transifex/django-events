# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="django-events",
    version="0.1a",
    description="Events in django applications.",
    author="Apostolis Bessas",
    author_email="mpessas@transifex.com",
    packages=["events"],
    install_requires=["Django", "django-appconf>=0.5"],
)
