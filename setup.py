from setuptools import setup, find_packages


version = '0.1.0'

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
        'django_pony_forms==0.3.5',
        'six'
    ],
    dependency_links=[
        "https://github.com/mbraak/django_pony_forms/archive/0.3.5.tar.gz#egg=django_pony_forms-0.3.5",
    ],
    author='Marco Braak',
    author_email='mbraak@ridethepony.nl',
)
