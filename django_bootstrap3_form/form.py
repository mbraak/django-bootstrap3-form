from django import forms

from django_pony_forms.pony_forms import PonyFormMixin


class BootstrapFormMixin(PonyFormMixin):
    form_template = 'django_bootstrap3_form/form.html'
    row_template = 'django_bootstrap3_form/row.html'
    errorlist_template = 'django_bootstrap3_form/errorlist.html'


class BootstrapForm(BootstrapFormMixin, forms.Form):
    pass