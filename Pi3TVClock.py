#
# Name: Pi3TVClock.py
# LANG: Python
# TARGET SYSTEM: Raspberry Pi 3 with OSMC
# Author: kigipaul (kigipaul@gmail.com)
# DATE: 2016/3

import os
import json
import time
import random
import RPi.GPIO as GPIO
from xbmcjson import XBMC, PLAYER_VIDEO

JSONRPC = "http://localhost:8080/jsonrpc"
ROOT_PATH = "/home/osmc/Movies/"
BIN_PATH = "bin"
MV_DIR = ["s1", "s2", "s3"]

for DIR in MV_DIR:
  if not os.path.dirname(ROOT_PATH + DIR):
    del MV_DIR[MV_DIR.index(DIR)]

MV_DIR_count = 0
get_mv_names = os.listdir(ROOT_PATH + MV_DIR[MV_DIR_count])
get_mv = ROOT_PATH + MV_DIR[MV_DIR_count] + "/" + \
    get_mv_names[random.randint(0, len(get_mv_names) - 1)]

TV_status = os.popen("./" + BIN_PATH + "/cec pow 0|grep 'standby'").read()[:-1]
time.sleep(3)

if not TV_status == "":
  os.system("./" + BIN_PATH + "/irsend send KEY_POWER")
  time.sleep(5)

xbmc = XBMC(JSONRPC)
xbmc.Player.Open({"item":{"file":get_mv}})

while True:
  TV_status = os.popen("./" + BIN_PATH + "/cec pow 0|grep 'standby'").read()[:-1]
  time.sleep(3)
  if not TV_status == "":
    os.system("./" + BIN_PATH + "/irsend send KEY_POWER")
    time.sleep(5)
