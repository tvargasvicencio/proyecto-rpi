from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^turnOn$', views.turnOn, name='turnOn'),
    url(r'^turnOff$', views.turnOff, name='turnOff'),
]
