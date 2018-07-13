# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import RPi.GPIO as GPIO
from utils import temhum
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
    return HttpResponse(json.dumps(json_response), content_type="application/json")
