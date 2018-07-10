# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import RPi.GPIO as GPIO

LED_PIN = 7

def turnOn(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(LED_PIN, 1)
    return HttpResponse('')


def turnOff(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(LED_PIN, 0)
    return HttpResponse('')

