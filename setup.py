from setuptools import setup, find_packages


version = '0.6.0'

setup(
    name='django-bootstrap3-form',
    version=version,
    license='Apache License, Version 2.0',
    description='Django-bootstrap3-form allows you write Django forms that work with Twitter Bootstrap 3',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django',
        'django_pony_forms',
        'six'
    ],
    author='Marco Braak',
    author_email='mbraak@ridethepony.nl',
    url='https://github.com/mbraak/django-bootstrap3-form',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
