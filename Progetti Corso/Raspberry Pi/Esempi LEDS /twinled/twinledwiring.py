import wiringpi
import time
from time import sleep

primoled = 14
secondoled = 18

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(primoled, wiringpi.OUTPUT)
wiringpi.pinMode(secondoled, wiringpi.OUTPUT)

while True:
        wiringpi.digitalWrite(primoled, wiringpi.HIGH)
        wiringpi.digitalWrite(secondoled, wiringpi.LOW)
        time.sleep(0.5)
        wiringpi.digitalWrite(primoled, wiringpi.LOW)
        wiringpi.digitalWrite(secondoled, wiringpi.HIGH)
        time.sleep(0.5)

