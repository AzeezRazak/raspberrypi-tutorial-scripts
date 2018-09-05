# Ensure that you run this script via local machine Python 3
# This script assumes you use Pin 12 for LED

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

for x in range(0, 5):
  print("LED ON")
  GPIO.output(12, GPIO.HIGH)
  time.sleep(0.5)
  
  print("LED OFF")
  GPIO.output(12, GPIO.LOW)
  time.sleep(0.5)
