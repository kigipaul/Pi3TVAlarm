import time
import os
import RPi.GPIO as GPIO

PIN = 18
COUNT = 0
END = 6
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

while True:
  if COUNT == END:
    COUNT = 0
    get_pid = os.popen('pgrep -f "^python Pi3TVClock.py"').read()[:-1]
    if not get_pid == "":
      os.system("kill -9 " + get_pid)
    print "Killed Pi3TVClock"
  if GPIO.input(PIN):
    COUNT += 1
  time.sleep(0.5)
