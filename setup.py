#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="extraer",
    author="Quantil SAS",
    version="0.1.0",
    packages=["extraer", "extraer.corpus"],
    install_requires=[
        'pandas',
        'pandarallel',
        'numpy',
        'nltk.corpus',
    ]
)
