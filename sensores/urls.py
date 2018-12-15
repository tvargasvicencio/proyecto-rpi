from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^temperatura-humedad$', views.temperatura_humedad, name='temperatura_humedad'),
    url(r'^encender_led/(?P<ledpin>[0-9]{2})/$', views.encender_led, name='encender_led'),
    url(r'^apagar_led/(?P<ledpin>[0-9]{2})/$', views.apagar_led, name='apagar_led'),
]

