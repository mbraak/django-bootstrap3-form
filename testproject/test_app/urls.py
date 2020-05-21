from django.urls import path

from . import views


urlpatterns = (
    path('', views.Example1.as_view(), name='example1'),
)
