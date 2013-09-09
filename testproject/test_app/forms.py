from django.core.exceptions import ValidationError

import django_bootstrap3_form


choices = (
    ('abc', 'Abc'),
    ('def', 'Def'),
    ('ghi', 'Ghi'),
)


class ExampleForm(django_bootstrap3_form.BootstrapForm):
    username = django_bootstrap3_form.CharField(placeholder='Enter username')
    password = django_bootstrap3_form.CharField(widget=django_bootstrap3_form.PasswordInput, placeholder='Enter password')
    choice = django_bootstrap3_form.BooleanField(required=False)
    text = django_bootstrap3_form.CharField(widget=django_bootstrap3_form.Textarea, placeholder='Enter text')
    options = django_bootstrap3_form.ChoiceField(choices)
    more_options = django_bootstrap3_form.ChoiceField(choices, widget=django_bootstrap3_form.RadioSelect, autofocus=True)
    date = django_bootstrap3_form.DateField()

    def clean(self):
        raise ValidationError('Error1')