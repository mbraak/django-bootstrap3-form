from django import forms

from .widgets import TextInput, CheckboxInput, Select, DateInput


class BooleanField(forms.BooleanField):
    widget = CheckboxInput

    def __init__(self, *args, **kwargs):
        self.autofocus = kwargs.pop('autofocus', None)

        super(BooleanField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(BooleanField, self).widget_attrs(widget)

        if self.autofocus:
            attrs['autofocus'] = self.autofocus

        return attrs


class CharField(forms.CharField):
    widget = TextInput

    def __init__(self, *args, **kwargs):
        self.placeholder = kwargs.pop('placeholder', None)
        self.autofocus = kwargs.pop('autofocus', None)

        super(CharField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(CharField, self).widget_attrs(widget)

        if self.placeholder:
            attrs['placeholder'] = self.placeholder

        if self.autofocus:
            attrs['autofocus'] = self.autofocus

        return attrs


class ChoiceField(forms.ChoiceField):
    widget = Select

    def __init__(self, *args, **kwargs):
        self.autofocus = kwargs.pop('autofocus', None)

        super(ChoiceField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(ChoiceField, self).widget_attrs(widget)

        if self.autofocus:
            attrs['autofocus'] = self.autofocus

        return attrs


class DateField(forms.DateField):
    widget = DateInput