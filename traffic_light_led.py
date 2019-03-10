# Ensure that you run this script via local machine Python 3
# This script assumes you use Pin 14 for Button
# This script assumes you use Pin 15 for Green LED
# This script assumes you use Pin 18 for Yellow LED
# This script assumes you use Pin 23 for Red LED
# This script assumes you use Pin 24 for Green LED Blinking

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)



while True:
  
  
  input_state = GPIO.input(18)
  if input_state == False:
    print("Button Pressed")
    time.sleep(0.2)
    
    print("LED ON")
    GPIO.output(15, GPIO.HIGH)
    time.sleep(0.5)

    print("LED OFF")
    GPIO.output(15, GPIO.LOW)
    time.sleep(0.5)
    
    print("LED ON")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)

    print("LED OFF")
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.5)
    
    print("LED ON")
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)

    print("LED OFF")
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)
    
    for x in range(0, 5):
      print("LED ON")
      GPIO.output(24, GPIO.HIGH)
      time.sleep(0.5)

      print("LED OFF")
      GPIO.output(24, GPIO.LOW)
      time.sleep(0.5)
