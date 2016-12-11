#!/usr/bin/env python
import sys
from setuptools import setup

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name='pycscart',
    version='1.0.5',
    description='CS-Cart Client Library',
    long_description="""
        Python interface to the CS-Cart or Multi-Vendor REST API.
    """,
    author='Gleb Goncharov',
    author_email='gongled@gongled.ru',
    install_requires=['requests>=2.0.0', 'packaging'],
    url='https://github.com/gongled/pycscart',
    packages=['pycscart', 'pycscart.entities'],
    license='MIT',
    platforms='Posix; MacOS X; Windows',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    **extra
)
