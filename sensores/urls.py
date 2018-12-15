from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^temperatura-humedad$', views.temperatura_humedad, name='temperatura_humedad'),
    url(r'^encender_led/(?P<pk>\d+)/$', views.encender_led, name='encender_led'),
    url(r'^apagar_led/(?P<pk>\d+)/$', views.apagar_led, name='apagar_led'),
]
