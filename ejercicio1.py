import RPi.GPIO as GPIO
import time
from sensores import distancia, led
from random import randint

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

def prenderSensor(sensor):
    led.encender(sensor["led"])
    distancia.detectarObstaculo(sensor["Trig"],sensor["Echo"])

if __name__ == '__main__':
    try:
        while True:
            sensor = sensores[randint(0,1)]
            start_time = time.time()
            led.encender(sensor["led"])
            midiendo = True
            while midiendo:
                resultado = distancia.detectarObstaculo(sensor["Trig"],sensor["Echo"])
                if resultado["medida"] <=5:
                    elapsed_time = time.time() - start_time
                    print "tiempo de reaccion: " + str(elapsed_time)
                    print "%.2f" %resultado["medida"] #por ultimo, vamos a mostrar el resultado por pantalla
                    led.apagar(sensor["led"])
                    midiendo = False
                    time.sleep(randint(0,3))
    except KeyboardInterrupt:
        print('LEDS OFF...\n')
        GPIO.output(sensores[0]["led"],GPIO.LOW)
        GPIO.output(sensores[1]["led"],GPIO.LOW)
        led.destroy(sensores[0]["led"])
        led.destroy(sensores[1]["led"])
