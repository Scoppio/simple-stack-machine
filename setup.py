# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "AbstractLang"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    description="AbstractLang",
    author_email="",
    url="",
    keywords=["Language", "Stack Machine"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    entry_points={
        'console_scripts': ['abstract=vm.abstract_cli:cli']},
    long_description="""\
    Abstract Lang
    """

)

