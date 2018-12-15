import RPi.GPIO as GPIO
import time

from mpu6050 import mpu6050

GPIO.setwarnings(False)
#set the gpio modes to board numbering
GPIO.setmode(GPIO.BOARD)

#setup function for some setup---custom function
def setup(LEDPIN):
    #set LEDPIN's mode to output,and initial level to LOW(0V)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)

def encender(LEDPIN):
    GPIO.output(LEDPIN,GPIO.HIGH)

def apagar(LEDPIN):
    GPIO.output(LEDPIN,GPIO.LOW)

#main function
def main(LEDPIN):
    #print info
    while True:
       encender(LEDPIN)
       print('...LED ON\n')
       time.sleep(0.5)

       apagar(LEDPIN)
       print('LED OFF...\n')
       time.sleep(0.5)
       pass
    pass

#define a destroy function for clean up everything after the script finished
def destroy(LEDPIN):
    #turn off LED
    GPIO.output(LEDPIN,GPIO.LOW)
    #release resource
    GPIO.cleanup()
#
# if run this script directly ,do:
if __name__ == '__main__':
    # set GPIO 0 as LED pin
    verde = 29
    amarillo = 35
    rojo = 33
    blanco = 31
    for a in [verde,amarillo,rojo,blanco]:
        setup(a)
    #setup(LEDPIN)
    sensor = mpu6050(0x68)
    try:
        #main(LEDPIN)
        while True:
            giro = sensor.get_accel_data()
            if giro['x']<5 and giro['x']>-5 and giro['y']<5 and giro['y']>-5 and giro['z']>0:
               encender(verde)
               apagar(amarillo)
               apagar(rojo)
               apagar(blanco)
            elif giro['x']>5 and giro['y']<5 and giro['y']>-5:
               apagar(verde)
               encender(amarillo)
               apagar(rojo)
               apagar(blanco)
            elif giro['x']<5 and giro['x']>-5 and giro['y']>5:
               apagar(verde)
               apagar(amarillo)
               encender(rojo)
               apagar(blanco)
            elif giro['x']<5 and giro['x']>-5 and giro['y']<-5:
               apagar(verde)
               apagar(amarillo)
               apagar(rojo)
               encender(blanco)
            else:
               apagar(verde)
               apagar(amarillo)
               apagar(rojo)
               apagar(blanco)
            time.sleep(1)
            print giro
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        for LEDPIN in [verde,amarillo,rojo,blanco]:
            GPIO.output(LEDPIN,GPIO.LOW)
            print('LED OFF...\n')
            destroy(LEDPIN)
