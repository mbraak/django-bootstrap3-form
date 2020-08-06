from setuptools import setup, find_packages

from os import path
from io import open

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

version = '1.1.0'

setup(
    name='django-bootstrap3-form',
    version=version,
    license='Apache License, Version 2.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Django-bootstrap3-form allows you write Django forms that work with Twitter Bootstrap 3',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django',
        'django_pony_forms'
    ],
    author='Marco Braak',
    author_email='mbraak@ridethepony.nl',
    url='https://github.com/mbraak/django-bootstrap3-form',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython"
    ]
)
