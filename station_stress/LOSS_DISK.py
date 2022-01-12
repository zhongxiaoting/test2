# coding=utf-8
import os
import time
from time import sleep
from config import constants as c
from utils import handle as h
from common import common_value as cv

class LOSS_DISK():
    cv.remove_log(c.LOSS_DISK_LOG_PATH)
    # 检查掉盘测试
    def run_item(self):
        sleep(30)
        disks = self.get_disk()
        write_log("==============  Loss Disk Check Begin " + get_local_time_string() + " =================")
        for i in range(10):
            fio = fio_run()
            memtester = mem_run()
            stress = stress_run()
            write_log("stress->> " + str(stress) + "   memtester->> " + str(memtester) + "   fio->> " + str(fio))
            if stress and memtester and fio:
                write_log("->>> CPU、Memory、Disks Stress Check is Running...")
                loss_or_not_disk = h.run_cmd("lsblk")
                write_log("->>> Disks Showing : ")
                write_log(loss_or_not_disk)
                if disks == loss_or_not_disk:
                    write_log("->>> Not Loss Disks! ")
                else:
                    write_log("->>> Disks Loss! ")
            else:
                write_log("->> stress、memtester and fio are Stopped!")
            write_log("=========== NO_" + str(i + 1) + " Loss Disk Check End " + get_local_time_string() + "  ===========")
            sleep(12)
        return

    def get_disk(self):
        disks = h.run_cmd("lsblk")
        return disks


def stress_run():
    stress = h.run_cmd("pidof stress")
    if "Fail" in stress:
        return None
    return stress


def mem_run():
    memtester = h.run_cmd("pidof memtester")
    if "Fail" in memtester:
        return None
    return memtester


def fio_run():
    fio = h.run_cmd("pidof fio")
    if "Fail" in fio:
        return None
    return fio


def write_log(s):
    with open(c.LOSS_DISK_LOG_PATH, 'a+') as f:
        print(s)
        f.write(str(s) + '\n')
        f.flush()
        os.fsync(f)


def get_local_time_string():
    return time.strftime('%04Y-%m-%d %H:%M:%S', time.localtime(time.time()))
