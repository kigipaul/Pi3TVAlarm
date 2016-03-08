#!/usr/bin/env python

# Author: kigipaul
# TARGET SYSTEM: Raspberry Pi 3 with OSMC
# DATE: 2016/3

import time
import os
import Pi3TVAlarm
import RPi.GPIO as GPIO

PIN = 18
COUNT = 0
END = 6
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

while True:
  if COUNT == END:
    COUNT = 0
    get_pid = os.popen('pgrep -f "^python Pi3TVAlarm.py"').read()[:-1]
    if not get_pid == "":
      os.system("kill -9 " + get_pid)
    TVctrl = Pi3TVAlarm.Pi3TVAlarm()
    TVctrl.turn_off_tv(TVctrl.check_tv_status())
    TVctrl.stop_mv()
    print "[DEBUG] Killed Pi3TVAlarm"
  if GPIO.input(PIN):
    COUNT += 1
  time.sleep(0.5)
