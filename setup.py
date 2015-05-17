#!/usr/bin/env python
import os
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = "Generates folders for coding dojo sessions"


def recursive_path(pack, path):
    matches = []
    for root, dirnames, filenames in os.walk(os.path.join(pack, path)):
        for filename in filenames:
            matches.append(os.path.join(root, filename)[len(pack) + 1:])
    return matches


print(find_packages(exclude=["dojogen/generators/*"]))

setup(
    name="dojogen",
    version="1.1.0",
    description="Generates folders for coding dojo sessions",
    long_description=long_description,
    packages = find_packages(exclude=["generators"]),
    package_data = {
        'dojogen': recursive_path('dojogen', 'generators'),
    },
    author = ("Joao Pimentel",),
    author_email = "joaofelipenp@gmail.com",
    license = "MIT",
    keywords = "dojo generate languages",
    url = "https://github.com/dojorio/dojogen",
    entry_points = {'console_scripts': ['dojogen = dojogen.dojogen:main']},
)
