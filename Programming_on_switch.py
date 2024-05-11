# programming on switch to control the LED - 7
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(23)
    if input_state == False:
        print('Button Pressed')
        GPIO.output(24,True)
        time.sleep(0.2)
    else:
        GPIO.output(24,False)