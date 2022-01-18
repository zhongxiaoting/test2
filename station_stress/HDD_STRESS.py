# coding=utf-8
import os
import re
import sys
import time

from main.item import Item
from utils import decorator, log as l
from config import constants as c
from common import common_value as cv

sys.path.append("..")


class HDD_STRESS(Item):
    def __init__(self, info):
        super(HDD_STRESS, self).__init__()
        self.info = info

    def run_item(self):
        self.make_up_raid()
        self.random_read_write()
        self.random_read()

    # 对每一个非系统盘进行读写测试
    @decorator.item_test
    def random_read_write(self):
        i = 1
        all_disk_not_os = self.remove_os_disk()
        write_log("========= Non-System Disk Read And Write Begin  " + get_local_time_string() + " ==========")
        for disk in all_disk_not_os:
            write_log("Begin NO." + str(i) + " the non-system disk read and write")
            shell = "fio -filename={} -direct=1 -iodepth 1" \
                    " -thread -rw=randrw -ioengine=psync -bs=16k" \
                    " -size=50% -numjobs=10 -runtime=20 -group_reporting" \
                    " -name=mytest_{}".format(disk, i)
            read_and_write = self.run_cmd(shell)
            # write_log("========== 开始对非系统盘进行读写测试 ==========")
            write_log("The Command Line ->>> " + shell + "\n")
            write_log(read_and_write)
            write_log("==================  NO." + str(i) + " non-system disk End ====================")
            i += 1
        write_log("->>> " + str(i - 1) + " non-system disks have been read and written End")
        return read_and_write

    # 对系统盘进行读测试
    @decorator.item_test
    def random_read(self):
        os_disk = self.get_os_disk()
        self.run_cmd("mkdir /test")
        shell = "fio -directory=/test -direct=1 -iodepth 1" \
                " -thread -rw=randread -ioengine=psync -bs=16k -size=2G" \
                " -numjobs=10 -runtime=20 -group_reporting -name=mytest_0"
        os_disk_read = self.run_cmd(shell)
        write_log("============ System Disk Read Begin  " + get_local_time_string() + " ==============")
        write_log("The Command Line->>> " + shell + "\n")
        write_log(os_disk_read)
        write_log("==============  System Disk Read End  " + get_local_time_string() + " =================")
        return os_disk_read

    # 是否要组Raid卡
    def make_up_raid(self):
        cv.remove_log(c.HDD_STRESS_LOG_PATH)
        write_log("=========== Disks Read and Write Check  " + get_local_time_string() + " ===============" + "\n")
        raid_or_not = self.run_cmd('lspci | grep "RAID" ')
        if "Fail" in raid_or_not or not raid_or_not:
            # write_log(raid_or_not)
            write_log("->>> No Raid")
        else:
            write_log("===================== Building Raid ============================")
            raid = self.run_cmd("sh makeraid0.sh")
            write_log("============== Build Raid Success, Information ==================")
            write_log(raid)
            write_log("==================================================================")
        return

    # 获取所有sd*,nvme*硬盘
    def get_all_disk(self):
        sd_disk = self.run_cmd('find /dev/ -name "sd*" | grep -E "sd[a-z]$" | sort ')
        nvme_disk = self.run_cmd('find /dev/ -name "nvme*" | grep -E "nvme[0-9][a-z][0-9]$" | sort ')
        if nvme_disk:
            all_disk = sd_disk + "\n" + nvme_disk
        else:
            all_disk = sd_disk
        return all_disk

    # 移除系统盘的所有盘
    def remove_os_disk(self):
        all_disk = self.get_all_disk().split()
        os_disk = self.get_os_disk()
        # print(all_disk)
        for disk in all_disk:
            os_disk_ = re.findall(os_disk, disk)
            for os in os_disk_:
                if os == os_disk:
                    remove_os = "/dev/" + os_disk
                    all_disk.remove(remove_os)
        write_log("->>> Tatol Non-system Disks: " + str(len(all_disk)))
        write_log("->>> Non-system Disks is : ")
        write_log(all_disk)
        return all_disk

    # 获取到系统盘
    def get_os_disk(self):
        i = 0
        os_disk = ""
        list_disk = []
        all_disk = self.run_cmd("lsblk")
        disk_list = all_disk.split("\n")
        # print(one_disk)
        for disk in disk_list:
            units = disk.split()
            # print(units)
            list_disk.append(units)
            if len(list_disk[i]) == 7:
                if list_disk[i][-1] == '/boot':
                    os_num = int(list_disk[i][0][-1])
                    os_disk = list_disk[i - os_num][0]
            i += 1
        write_log("->>> System Disk is : " + os_disk)
        return os_disk

    # # 检车测试项的log中是否有fail项目
    # def check_log(self):
    #     with open("result.log", "r") as f:
    #         data = f.read()
    #         error1 = re.findall("fail", data)
    #         error2 = re.findall("error", data)
    #         error3 = re.findall("Fail", data)
    #         if error1 or error2 or error3:
    #             write_log("->> 测试项目中有fail项目，请检查！")
    #             # l.log(str(error1) + "\n" + str(error2) + "\n" + str(error3))
    #             return
    #     write_log("->> 测试项目通过测试！")
    #     return


def write_log(s):
    with open(c.HDD_STRESS_LOG_PATH, 'a+') as f:
        print(s)
        f.write(str(s) + '\n')
        f.flush()
        os.fsync(f)


def get_local_time_string():
    return time.strftime('%04Y-%m-%d %H:%M:%S', time.localtime(time.time()))
