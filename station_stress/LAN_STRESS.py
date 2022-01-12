# coding=utf-8
import os
import re
import sys
import time
from config import constants as c
from main.item import Item
from common import common_value as cv

sys.path.append("..")


# CMD_GET_ETH_INFORMATION
class LAN_STRESS(Item):
    def __init__(self, info):
        self.info = info

    def run_item(self):
        self.start_lan_run()

    def start_lan_run(self):
        cv.remove_log(c.LAN_STRESS_LOG_PATH)
        write_log("=============  LAN Stress Check Begin  " + get_local_time_string() + " ================")
        self.run_cmd("sh /home/test2/lan_stress/eth.sh")
        write_log("==============  LAN Stress Check End  " + get_local_time_string() + " =================")


def write_log(s):
    with open(c.LAN_STRESS_LOG_PATH, 'a+') as f:
        print(s)
        f.write(str(s) + '\n')
        f.flush()
        os.fsync(f)


def get_local_time_string():
    return time.strftime('%04Y-%m-%d %H:%M:%S', time.localtime(time.time()))
