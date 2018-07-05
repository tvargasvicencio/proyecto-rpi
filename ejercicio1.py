import RPi.GPIO as GPIO
import time
from sensores import distancia, led

GPIO.setwarnings(False)
#set the gpio modes to board numbering
GPIO.setmode(GPIO.BOARD)

LEDPIN = 7
Trig = 11
Echo = 13

led.setup(LEDPIN)
distancia.setup(Trig,Echo)

if __name__ == '__main__':
    try:
        main(LEDPIN)
    except KeyboardInterrupt:
        print('LED OFF...\n')
        distancia.destroy(LEDPIN)