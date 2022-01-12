# coding=utf-8
import os
import re
import sys
import threading
import time

from main.item import Item
from CPU_STRESS import CPU_STRESS
from MEM_STRESS import MEM_STRESS
from HDD_STRESS import HDD_STRESS
from LOSS_DISK import LOSS_DISK
from check_log import ALL_STRESS_LOG
from LAN_STRESS import LAN_STRESS

sys.path.append("..")

"""
All Stress Ckeck 
"""


class STRESS_ALL(Item):
    def __init__(self, info):
        super(STRESS_ALL, self).__init__()
        self.info = info

    def run_item(self):
        self.all_stress_check()
        # LOSS_DISK().run_item()

    def all_stress_check(self):
        items_run = []
        items = ['CPU_STRESS', 'MEM_STRESS', 'HDD_STRESS', 'LAN_STRESS', 'LOSS_DISK', 'check_all']
        for item in items:
            items_run.append(self.get_item_by_name(item))
        for stress_item in items_run:
            t = threading.Thread(target=stress_item.run_item)
            # t.setDaemon(True)
            t.start()
        return

    def get_item_by_name(self, name):
        if name == "CPU_STRESS":
            return CPU_STRESS(Item)
        if name == "MEM_STRESS":
            return MEM_STRESS(Item)
        if name == 'HDD_STRESS':
            return HDD_STRESS(Item)
        if name == 'LAN_STRESS':
            return LAN_STRESS(Item)
        if name == 'LOSS_DISK':
            return LOSS_DISK()
        if name == 'check_all':
            return ALL_STRESS_LOG()



