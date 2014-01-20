#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


with open('README.rst') as readme:
    long_description = readme.read()


with open('requirements.txt') as requirements:
    lines = requirements.readlines()
    libraries = [lib for lib in lines if not lib.startswith('-')]
    dependency_links = [link.split()[1] for link in lines if
        link.startswith('-f')]


setup(
    name = 'django-rest-framework-utils',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = libraries,
    dependency_links = dependency_links,
    long_description = long_description,
    author = 'Arnaud Grausem',
    author_email = 'arnaud.grausem@unistra.fr',
    maintainer = 'Arnaud Grausem',
    maintainer_email = 'arnaud.grausem@unistra.fr',
    description = 'Utilities for the Django Rest Framework',
    keywords = ['django', 'REST', 'rest_framework', 'permissions'],
    url = 'https://github.com/unistra/django-rest-framework-utils',
    download_url = 'https://pypi.python.org/pypi/django-rest-framework-utils',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ]
)
