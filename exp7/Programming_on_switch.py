# programming on switch to control the LED - 7
import RPi.GPIO as GPIO
import time
INPUT_PIN=18
OUTPUT_PIN=23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT_PIN,GPIO.OUT)
GPIO.setup(INPUT_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(INPUT_PIN)
    if input_state == False:
        print('Button Pressed')
        GPIO.output(OUTPUT_PIN,True)
        time.sleep(0.2)
    else:
        GPIO.output(OUTPUT_PIN,False)