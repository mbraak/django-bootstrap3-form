# Django Bootstrap 3 form

[![Build Status](https://travis-ci.org/mbraak/django-bootstrap3-form.png)](https://travis-ci.org/mbraak/django-bootstrap3-form) [![Coverage Status](https://coveralls.io/repos/mbraak/django-bootstrap3-form/badge.png)](https://coveralls.io/r/mbraak/django-bootstrap3-form) [![Downloads](https://pypip.in/d/django-bootstrap3-form/badge.png)](https://pypi.python.org/pypi/django-bootstrap3-form/) [![Version](https://pypip.in/v/django-bootstrap3-form/badge.png)](https://pypi.python.org/pypi/django-bootstrap3-form/) [![Requirements Status](https://requires.io/github/mbraak/django-bootstrap3-form/requirements.png?branch=master)](https://requires.io/github/mbraak/django-bootstrap3-form/requirements/?branch=master)

**Django-bootstrap3-form** allows you write Django forms that work with Twitter Bootstrap 3.

It supports Django 1.4-1.8.

```python
import django_bootstrap3_form

class ExampleForm(django_bootstrap3_form.BootstrapForm):
	username = django_bootstrap3_form.CharField()
	password = django_bootstrap3_form.CharField(widget=django_bootstrap3_form.PasswordInput)
```
