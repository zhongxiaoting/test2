# coding=utf-8
import os
import sys
import time
from time import sleep
from config import constants as c
from utils import handle as h, log as l
from common import common_value as cv

class LOSS_DISK():
    cv.remove_log(c.LOSS_DISK_LOG_PATH)
    # 检查掉盘测试
    def run_item(self):
        i = 1
        sleep(300)
        disks = self.get_disk()
        write_log("==============  Loss Disk Check Begin " + get_local_time_string() + " =================")
        while True:
            fio = fio_run()
            memtester = mem_run()
            stress = stress_run()
            # print("stress->> " + str(stress) + "   memtester->> " + str(memtester) + "   fio->> "
            #           + str(fio))
            if stress and memtester and fio:
                write_log("->>> CPU、Memory、Disks、LAN Stress Check is Running...")
                loss_or_not_disk = h.run_cmd("lsblk")
                write_log("->>> Disks Showing : ")
                write_log(loss_or_not_disk)
                if disks == loss_or_not_disk:
                    write_log("->>> Not Loss Disks! ")
                else:
                    write_log("->>>ERROR, Disks Loss! ")
                    l.fail_msg("Disk Loss Check have ERROR, Please check progress!")
                    sys.exit(1)
                    break
            else:
                write_log("->> stress、memtester 、fio and lan are Stopped!")
                break
            write_log("=========== NO_" + str(i) + " Loss Disk Check End " + get_local_time_string() + "  ===========")
            i += 1
            sleep(3600)
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
