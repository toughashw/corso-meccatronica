import RPi.GPIO as GPIO
import time
from time import sleep

primoled = 14
secondoled = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(primoled, GPIO.OUT)
GPIO.setup(secondoled, GPIO.OUT)

while True:
        GPIO.output(primoled, GPIO.HIGH)
        GPIO.output(secondoled, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(primoled, GPIO.LOW)
        GPIO.output(secondoled, GPIO.HIGH)
        time.sleep(0.5)