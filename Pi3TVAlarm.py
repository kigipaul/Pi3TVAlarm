#!/usr/bin/env python

# Author: kigipaul
# TARGET SYSTEM: Raspberry Pi 3 with OSMC
# DATE: 2016/3

import os
import time
import random
from xbmcjson import XBMC, PLAYER_VIDEO


class Pi3TVAlarm(object):
  def __init__(self):
    self.JSONRPC = "http://localhost:8080/jsonrpc"
    self.xbmc = XBMC(self.JSONRPC)
    self.ROOT_PATH = "/home/osmc/Movies/"
    self.BIN_PATH = "bin"
    self.MV_DIR = ["s1", "s2", "s3"]
    self.MV_DIR_count = 0
    self.ON_TV_GAP = 12
    self.SLEEP_TIME = 10

    for DIR in self.MV_DIR:
      if not os.path.dirname(self.ROOT_PATH + DIR):
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
    time.sleep(4)
    return TV_status

  def turn_off_tv(self, status):
    if status == "":
      os.system("./" + self.BIN_PATH + "/irsend send KEY_POWER")

  def turn_on_tv(self, status, action = 0):
    if not status == "":
      if action == 1:
        self.MV_DIR_count += 1
        # Actions when all video played
        if self.MV_DIR_count >= len(self.MV_DIR):
          self.MV_DIR_count = len(self.MV_DIR) - 1
          self.SLEEP_TIME = 0
      os.system("./" + self.BIN_PATH + "/irsend send KEY_POWER")
      time.sleep(self.ON_TV_GAP)
      self.start_mv(self.get_mv())
    return True

  def start_mv(self, path):
    self.xbmc.Player.Open({"item":{"file":path}})
    time.sleep(1)
    get_player = self.xbmc.Player.GetActivePlayers()["result"]
    if get_player:
      self.xbmc.Player.SetRepeat({"playerid":get_player[0]["playerid"]})

  def stop_mv(self):
    get_player = self.xbmc.Player.GetActivePlayers()["result"]
    if get_player:
      self.xbmc.Player.Stop({"playerid":get_player[0]["playerid"]})

  def run(self):
    self.turn_on_tv(self.check_tv_status())
    while self.turn_on_tv(self.check_tv_status(), 1):
      time.sleep(self.SLEEP_TIME)

if __name__ == "__main__":
  Pi3TVAlarm().run()

