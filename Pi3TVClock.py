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


class Pi3TVClock(object):
  def __init__(self):
    self.JSONRPC = "http://localhost:8080/jsonrpc"
    self.xbmc = XBMC(JSONRPC)
    self.ROOT_PATH = "/home/osmc/Movies/"
    self.BIN_PATH = "bin"
    self.MV_DIR = ["s1", "s2", "s3"]
    self.MV_DIR_count = 0

    for DIR in self.MV_DIR:
      if not os.path.dirname(self.ROOT_PATH + self.DIR):
        del self.MV_DIR[self.MV_DIR.index(DIR)]

  def get_mv(self):
    mv_path = self.ROOT_PATH + self.MV_DIR[self.MV_DIR_count]
    get_mv_names = os.listdir(mv_path)
    get_mv = mv_path + "/" + \
            get_mv_names[random.randint(0, len(get_mv_names) - 1)]
    return get_mv

  def check_tv_status(self):
    TV_status = os.popen("./" + self.BIN_PATH + \
            "/cec pow 0|grep 'standby'").read()[:-1]
    time.sleep(3)
    return TV_status

  def turn_on_tv(self, status, action = 0):
    if not status == "":
      os.system("./" + BIN_PATH + "/irsend send KEY_POWER")
      time.sleep(10)
      if action == 1:
        self.MV_DIR_count += 1
        if self.MV_DIR_count >= len(MV_DIR):
          return False
      self.start_mv(self.get_mv)
    return True

  def start_mv(self, path)
    self.xbmc.Player.Open("item":{"file":path})

  def run(self):
    self.turn_on_tv(self.check_tv_status)
    while self.turn_on_tv(self.check_tv_status, 1):
      continue

if __name__ == "__main__":
  Pi3TVClock().run()

