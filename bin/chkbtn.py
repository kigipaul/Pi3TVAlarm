#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

PIN=18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

while True:
  if GPIO.input(PIN):
    print "btn click"
  time.sleep(0.4)

