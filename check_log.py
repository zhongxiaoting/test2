# coding=utf-8
import os
import re
import time
import time as t
from config import constants as c
from station_stress import LOSS_DISK


class ALL_STRESS_LOG():

    def run_item(self):
        self.backup_log()
        while True:
            stress = LOSS_DISK.stress_run()
            memtester = LOSS_DISK.mem_run()
            fio = LOSS_DISK.fio_run()
            if stress is None and memtester is None and fio is None:
                print("check_stress->> " + str(stress) + "   memtester->> " + str(memtester) + "   fio->> " + str(fio))
                self.read_cpu_log()
                self.read_mem_log()
                self.read_hdd_log()
                self.check_log()
                break

    # backup stress.log
    def backup_log(self):
        if os.path.exists(c.STRESS_ALL_LOG):
            # print(11)
            os.rename(c.STRESS_ALL_LOG, c.STRESS_LOG + '/stress/' + self.get_local_time_string() + '.log')

    def read_cpu_log(self):
        with open(c.CPU_STRESS_LOG_PATH, "r") as f:
            cpu_data = f.read()
        self.write_log("The server serial number is: " + c.get_sn())
        self.write_log("===============  STRESS_ALL " + self.get_local_time_string() + "=======================")
        self.write_log(cpu_data)
        return cpu_data

    def read_mem_log(self):
        with open(c.MEM_STRESS_LOG_PATH, "r") as f:
            mem_data = f.read()
        self.write_log(str(mem_data) + '\n')
        return mem_data

    def read_hdd_log(self):
        with open(c.HDD_STRESS_LOG_PATH, "r") as f:
            hdd_data = f.read()
        self.write_log(str(hdd_data) + '\n')
        return hdd_data

    def write_log(self, s):
        with open(c.STRESS_ALL_LOG, 'a+') as f:
            f.write(str(s) + '\n')
            f.flush()
            os.fsync(f)

    # 检查测试项的log中是否有fail项目
    def check_log(self):
        with open(c.STRESS_ALL_LOG, "r") as f:
            data = f.read()
            error1 = re.findall("fail", data)
            error2 = re.findall("error", data)
            error3 = re.findall("Fail", data)
            if error1 or error2 or error3:
                self.write_log("->> 测试项目中有fail项目，请检查！")
                # l.log(str(error1) + "\n" + str(error2) + "\n" + str(error3))
                return
        self.write_log("->> 测试项目通过测试！")
        # print("->> 测试项目通过测试！")
        return

    def get_local_time_string(self):
        return time.strftime('%04Y-%m-%d %H:%M:%S', time.localtime(time.time()))


# if __name__ == "__main__":
#     check = ALL_STRESS_LOG()
#     check.run_item()
