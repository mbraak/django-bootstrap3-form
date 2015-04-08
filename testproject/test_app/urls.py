from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^$', views.Example1.as_view(), name='example1'),
)
