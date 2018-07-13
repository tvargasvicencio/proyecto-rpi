# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import RPi.GPIO as GPIO
from utils import temhum

def temperatura_humedad(request):
    hola = temhum.read_dht11_dat()
    return HttpResponse(''+hola)