from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.Example1.as_view(), name='example1')
)
