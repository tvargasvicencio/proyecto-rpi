import RPi.GPIO as GPIO
import time
from sensores import distancia, led

GPIO.setwarnings(False)
#set the gpio modes to board numbering
GPIO.setmode(GPIO.BOARD)

LEDS = {
    "led1": 7,
    "led2": 12
}
US = {
    "us1":{
        "Trig": 11,
        "Echo": 13
    },
    "us2":{
        "Trig": 16,
        "Echo": 18
    }
}

led.setup(LEDS["led1"])
led.setup(LEDS["led2"])
distancia.setup(US["us1"]["Trig"],US["us1"]["Echo"])
distancia.setup(US["us2"]["Trig"],US["us2"]["Echo"])

if __name__ == '__main__':
    try:
        led.main(LEDS["led2"])
    except KeyboardInterrupt:
        print('LED OFF...\n')
        GPIO.output(LEDS["led1"],GPIO.LOW)
        GPIO.output(LEDS["led2"],GPIO.LOW)
	led.destroy(LEDS["led1"])
        led.destroy(LEDS["led2"])
