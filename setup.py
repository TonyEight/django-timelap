#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
import timelap
 
# Ceci n'est qu'un appel de fonction. Mais il est trèèèèèèèèèèès long
# et il comporte beaucoup de paramètres
setup(
    name='timelap',
    version=timelap.__version__,
    packages=find_packages(),
    author="TonyEight",
    author_email="ludovic.legendart@gmail.com",
    description="Brings start and end dates to Django models",
    long_description=open('README.md').read(),
    install_requires=["django >= 1.7"],
    include_package_data=True,
    url='http://github.com/TonyEight/django-timelap',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)