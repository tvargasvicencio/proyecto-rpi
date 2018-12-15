import RPi.GPIO as GPIO
import time

# set BCM_GPIO 17(GPIO 0) as PIR pin
PIRPin = 11
LEDPIN = 40

#print message at the begining ---custom function
def print_message():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

#setup function for some setup---custom function
def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BOARD numbering
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIRPin,GPIO.IN)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)

#main function
def main():
    #print info
    print_message()
    while True:
        #read Sw520dPin's level
        if(GPIO.input(PIRPin)!=0):
            #time.sleep(0.5)
            print ('*     alarm!     *')
            print ('\n')
            GPIO.output(LEDPIN,GPIO.HIGH)
            time.sleep(1)
        else:
            #print ('=     Not alarm...  =')
            #print ('\n')
            GPIO.output(LEDPIN,GPIO.LOW)
            time.sleep(0.1)

#define a destroy function for clean up everything after the script finished
def destroy():
    #release resource
    GPIO.output(LEDPIN,GPIO.LOW)
    GPIO.cleanup()
#
# if run this script directly ,do:
if __name__ == '__main__':
    setup()
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()
        pass
