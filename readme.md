# Django Bootstrap 3 form

**Django-bootstrap3-form** allows you write Django forms that work with Twitter Bootstrap 3.

```
import django_bootstrap3_form

class ExampleForm(django_bootstrap3_form.BootstrapForm):
	username = django_bootstrap3_form.CharField()
	password = django_bootstrap3_form.CharField(widget=django_bootstrap3_form.PasswordInput)
```