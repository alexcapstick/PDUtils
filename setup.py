import os
from setuptools import setup, find_packages
import subprocess
import logging
from pdu import __version__, __doc__, __author__, __title__, __author_email__

PACKAGE_NAME = 'pdu'


setup(
    name=__title__,
    version=__version__,
    description=__doc__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    long_description=open('README.txt').read(),
    install_requires=[
    ]
)