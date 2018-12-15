# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import RPi.GPIO as GPIO
from utils import temhum, led
import json

def temperatura_humedad(request):
    dato = temhum.read_dht11_dat(8) # conectado a BOARD 8
    intentos = 1
    while dato == False:
        dato = temhum.read_dht11_dat(8)
        intentos += 1
    json_response = {
        "temperatura":dato["temperatura"],
        "humedad":dato["humedad"],
        "intentos":intentos,
    }
    GPIO.cleanup() # cleanup all GPIO
    return HttpResponse(json.dumps(json_response), content_type="application/json")

def encender_led(request,ledpin):
    led.setup(int(ledpin))
    led.encender(int(ledpin))
    return HttpResponse(json.dumps({"result":True}), content_type="application/json")

def apagar_led(request,ledpin):
    led.setup(int(ledpin))
    led.apagar(int(ledpin))
    return HttpResponse(json.dumps({"result":True}), content_type="application/json")
