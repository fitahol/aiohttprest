#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '05/01/2017'
__author__ = 'deling.ma'
"""
import os
import re
from setuptools import setup


with open('aiohttp-rest-framework/__init__.py') as f:
    version = re.search(r'__version__\s*=\s*\'(.+?)\'', f.read()).group(1)
assert version


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name="aiohttp-rest-framework",
    version=version,
    packages=get_packages('aio_rest'),
    package_data=get_package_data('aio_rest'),
    install_requires=["aiohttp>=1.1", "Jinja2>=2.8", "pyyaml>=3.12",
                      "SQLAlchemy>=1.1.0", "aioodbc>=0.0.3"],
    tests_require=["pytest==2.8.3", "pytest-cov==2.2.0"],
    author="Devin Mah",
    author_email="lingnck@gmail.com",
    description="aiohttp rest framework.",
    url="http://github.com/lingnck/aiohttp-rest-framework",
)
