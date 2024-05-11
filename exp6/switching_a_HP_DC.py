import RPi.GPIO as GPIO
import time
relay_pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)
for i in range(4):
    GPIO.output(relay_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(relay_pin, GPIO.HIGH)
    time.sleep(1)
GPIO.cleanup()