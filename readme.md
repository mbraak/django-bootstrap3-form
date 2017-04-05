# Django Bootstrap 3 form

[![Build Status](https://travis-ci.org/mbraak/django-bootstrap3-form.svg?branch=master)](https://travis-ci.org/mbraak/django-bootstrap3-form) [![Version](https://badge.fury.io/py/django-bootstrap3-form.svg)](https://pypi.python.org/pypi/django-bootstrap3-form/)

[![Coverage Status](https://img.shields.io/coveralls/mbraak/django-bootstrap3-form.svg)](https://coveralls.io/r/mbraak/django-bootstrap3-form?branch=master) [![Downloads](https://img.shields.io/pypi/dm/django-bootstrap3-form.svg)](https://pypi.python.org/pypi/django-bootstrap3-form/) [![Requirements Status](https://requires.io/github/mbraak/django-bootstrap3-form/requirements.svg?branch=master)](https://requires.io/github/mbraak/django-bootstrap3-form/requirements/?branch=master)

[![License](https://img.shields.io/pypi/l/django-bootstrap3-form.svg)](https://pypi.python.org/pypi/django-bootstrap3-form/)

**Django-bootstrap3-form** allows you write Django forms that work with Twitter Bootstrap 3.

It supports Django 1.8-1.11. Also tested with Python 2.7, 3.3 - 3.6.

Note that version 0.3.0 also supports Django 1.7.

```python
import django_bootstrap3_form

class ExampleForm(django_bootstrap3_form.BootstrapForm):
	username = django_bootstrap3_form.CharField()
	password = django_bootstrap3_form.CharField(widget=django_bootstrap3_form.PasswordInput)
```

[![Code Issues](https://www.quantifiedcode.com/api/v1/project/0f951eae2c1144989a444aa9d237fc0c/badge.svg)](https://www.quantifiedcode.com/app/project/0f951eae2c1144989a444aa9d237fc0c)
