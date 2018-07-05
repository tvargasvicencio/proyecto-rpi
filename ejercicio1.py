import RPi.GPIO as GPIO
import time
from sensores import distancia, led

GPIO.setwarnings(False)
#set the gpio modes to board numbering
GPIO.setmode(GPIO.BOARD)

sensores = [
    {
    "led": 7,
    "Trig": 11,
    "Echo": 13
    },
    {
    "led": 12,
    "Trig": 16,
    "Echo": 18
    },

]

led.setup(sensores[0]["led"])
led.setup(sensores[1]["led"])
distancia.setup(sensores[0]["Trig"],sensores[0]["Echo"])
distancia.setup(sensores[1]["Trig"],sensores[1]["Echo"])

if __name__ == '__main__':
    try:
        led.main(sensores[0]["led"])
    except KeyboardInterrupt:
        print('LEDS OFF...\n')
        GPIO.output(sensores[0]["led"],GPIO.LOW)
        GPIO.output(sensores[1]["led"],GPIO.LOW)
        led.destroy(sensores[0]["led"])
        led.destroy(sensores[1]["led"])
