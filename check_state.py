# Ensure that you run this script via local machine Python 3
# This script assumes you use Pin 12 for LED

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, GPIO.HIGH)
state = GPIO.input(12)
print(state)
