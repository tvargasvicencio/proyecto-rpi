import RPi.GPIO as GPIO
import time

# set GPIO 0 as LED pin
LEDPIN = 7


#setup function for some setup---custom function
def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to board numbering
    GPIO.setmode(GPIO.BOARD)
    #set LEDPIN's mode to output,and initial level to LOW(0V)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)

#main function
def main():
    #print info
    print_message()
    while True:
       GPIO.output(LEDPIN,GPIO.HIGH)
       print('...LED ON\n')
       time.sleep(0.5)

       GPIO.output(LEDPIN,GPIO.LOW)
       print('LED OFF...\n')
       time.sleep(0.5)
       pass
    pass

#define a destroy function for clean up everything after the script finished
def destroy():
    #turn off LED
    GPIO.output(LEDPIN,GPIO.LOW)
    #release resource
    GPIO.cleanup()
#
# if run this script directly ,do:
if __name__ == '__main__':
    setup()
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        GPIO.output(LEDPIN,GPIO.LOW)
        print('LED OFF...\n')
        destroy()
