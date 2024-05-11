# experiment 8
import RPi.GPIO as GPIO
from time import sleep

button_pin1=17
button_pin2=18
led_pin=27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

def turn_on_led(channel):
    GPIO.output(led_pin, GPIO.HIGH)
    print('switch 1 rising, led on')
def turn_off_led(channel):
    GPIO.output(led_pin, GPIO.LOW)
    print('switch 2 falling, led off')


GPIO.add_event_detect(button_pin1, GPIO.RISING, callback=turn_on_led, bouncetime=200)
GPIO.add_event_detect(button_pin2, GPIO.FALLING, callback=turn_off_led, bouncetime=200)
try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO cleanup completed')