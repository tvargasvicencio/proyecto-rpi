from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^temperatura-humedad$', views.temperatura_humedad, name='temperatura_humedad'),
]
