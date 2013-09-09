from django.template import Context
from django.template.loader import get_template


class FormControlMixin(object):
    css_class = 'form-control'

    def render(self, name, value, attrs=None):
        attrs = attrs or dict()

        class_string = self._get_class_string(attrs)

        if class_string:
            attrs['class'] = class_string

        return super(FormControlMixin, self).render(name, value, attrs)

    def _get_class_string(self, attrs):
        classes = []
        if 'class' in attrs:
            classes.append(attrs['class'])

        classes += get_list(self.css_class)

        return ' '.join(classes)


def get_list(v):
    if not v:
        return []
    elif isinstance(v, (list, tuple)):
        return v
    else:
        return [v]


class TemplatedWidget(object):
    template_name = None

    def render(self, name, value, attrs=None, label=None):
        template = self.get_template()

        context = Context(
            self.get_context(name, value, attrs, label)
        )

        return template.render(context)

    def get_context(self, name, value, attrs, label=None):
        return dict(
            name=name,
            value=value,
            attr=attrs,
            label=label,
        )

    def get_template(self):
        if not hasattr(self, '_template'):
            self._template = get_template(self.template_name)

        return self._template