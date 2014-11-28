from django import forms
from django.forms import widgets
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

try:
    # >= Django 1.7
    from django.forms.utils import flatatt
except ImportError:
    # <= Django 1.6
    from django.forms.util import flatatt

from .util import FormControlMixin, TemplatedWidget


class CheckboxInput(TemplatedWidget, forms.CheckboxInput):
    template_name = 'django_bootstrap3_form/checkbox_widget.html'
    renders_label = True

    def get_context(self, name, value, attrs, label=None):
        context = super(CheckboxInput, self).get_context(name, value, attrs, label)

        context['checked'] = self.check_test(value)
        context['label'] = label

        if not (value is True or value is False or value is None or value == ''):
            context['value'] = force_text(value)

        if attrs:
            context['attrs'] = mark_safe(flatatt(attrs))

        return context


class PasswordInput(FormControlMixin, forms.PasswordInput):
    pass


class TextInput(FormControlMixin, forms.TextInput):
    pass


class Textarea(FormControlMixin, forms.Textarea):
    pass


class Select(FormControlMixin, forms.Select):
    pass


class RadioSelect(TemplatedWidget, forms.RadioSelect):
    template_name = 'django_bootstrap3_form/radio_select_widget.html'
    renders_label = True

    def get_context(self, name, value, attrs, label=None):
        context = super(RadioSelect, self).get_context(name, value, attrs, label)

        if value is None:
            value = ''

        context.update(
            selected_value=force_text(value),
            attrs=self.build_attrs(attrs),
            options=self.get_options(value),
        )

        return context

    def get_options(self, selected_value):
        selected_value = force_text(selected_value)

        def get_option(value, title):
            value = force_text(value)

            return dict(
                value=value,
                title=title,
                checked=(value == selected_value),
            )

        return [
            get_option(value, title) for value, title in self.choices
        ]


class DateInput(FormControlMixin, widgets.DateInput):
    input_type = 'date'

    def __init__(self, attrs=None, format_=None):
        # Html 5 date input expects this format
        format_ = format_ or '%Y-%m-%d'

        widgets.DateInput.__init__(self, attrs, format_)


class NumberInput(TextInput):
    input_type = 'number'
