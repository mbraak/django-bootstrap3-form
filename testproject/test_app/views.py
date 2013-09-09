from django.views import generic

from .forms import ExampleForm


class Example1(generic.FormView):
    template_name = 'example1.html'
    form_class = ExampleForm