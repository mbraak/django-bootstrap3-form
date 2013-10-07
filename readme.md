# Django Bootstrap 3 form

[![Build Status](https://travis-ci.org/mbraak/django-bootstrap3-form.png)](https://travis-ci.org/mbraak/django-bootstrap3-form)

[![Coverage Status](https://coveralls.io/repos/mbraak/django-bootstrap3-form/badge.png)](https://coveralls.io/r/mbraak/django-bootstrap3-form)

**Django-bootstrap3-form** allows you write Django forms that work with Twitter Bootstrap 3.

```
import django_bootstrap3_form

class ExampleForm(django_bootstrap3_form.BootstrapForm):
	username = django_bootstrap3_form.CharField()
	password = django_bootstrap3_form.CharField(widget=django_bootstrap3_form.PasswordInput)
```