#!/usr/bin/env python
# -*- coding: utf-8 -*-

# as inspired by https://github.com/kennethreitz/setup.py

from __future__ import absolute_import, unicode_literals
import codecs
import os
from setuptools import setup

from scrapyjobparameters import __package__, __version__


packages = [
    __package__,
]

REQUIRED = [
    'scrapy',
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANFEST.in file!
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name=__package__,
    version=__version__,
    description='Scrapy extension to make job_id and project_id available as spider fields.',
    long_description=long_description,
    author='Jean Maynier',
    author_email='jmaynier@kpler.com',
    url='http://github.com/kpler/scrapy-job-parameters-extension',
    packages=packages,
    install_requires=REQUIRED,
    include_package_data=True,
    classifiers=(
        'Development Status :: 4 - Beta'
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ),
)
