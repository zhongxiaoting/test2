# coding=utf-8

import commands
import os.path




def get_sn():
    # ret = commands.getstatusoutput('ipmitool fru print 0 | grep "Product Serial" | awk -F ":" \'{print $2}\' ')
    # if ret[0] == 0:
    #     return ret[1].strip()
    # else:
    sn = raw_input("Please input server serial number: ")
    return sn


sn_path = get_sn()
def stress_dir():
    make_dir = commands.getstatusoutput('mkdir %s' % (sn_path))
    return make_dir[0]


if not os.path.exists('/home/test2/' + sn_path):
    stress_path = stress_dir()


###############
# 1. dir and path
###############
# define test root path
TEST_DIR = '/home/test2'
STRESS_LOG = TEST_DIR + '/' + sn_path
LOG_BACKUP_DIR = TEST_DIR + '/log_backup'
CFG_PATH = TEST_DIR + '/cfg.json'
RESULT_LOG_PATH = TEST_DIR + '/result.log'
FULL_LOG_PATH = TEST_DIR + '/full.log'
CONTROLLER_JSON_PATH = TEST_DIR + '/main/controller.json'
CPU_STRESS_LOG_PATH = STRESS_LOG + '/cpu_stress.log'
MEM_STRESS_LOG_PATH = STRESS_LOG + '/mem_stress.log'
HDD_STRESS_LOG_PATH = STRESS_LOG + '/'
LAN_STRESS_LOG_PATH = STRESS_LOG + '/lan_stress.log'
MCE_ECC_LOG = STRESS_LOG + '/mce_ecc.log'
LOSS_DISK_LOG_PATH = STRESS_LOG + '/loss_disk.log'
STRESS_ALL_LOG = TEST_DIR + '/' + sn_path + '.log'
BLACK_LIST_LOG = TEST_DIR + '/blacklistall.log'

# run time
RUN_SECONDS = 86400



###############
# 2. variable
###############
# define sn  number minimum value
SN_MINI_NUMBER= 6

# define operator number minimum value
OPERATOR_MINI_NUMBER = 4


###############
# 3. network
###############
# MES host url and port
# MES_HOST = 'http://localhost:3000'

# state = 1 is normal state
STATE_OK = 1

# get hardware info path
# HW_CFG = MES_HOST + '/public/hw_cfg.json'

# upload hardware info path
# UPLOAD_HW_CFG = MES_HOST + '/hw_cfg'

# upload hardware info local path
LOCAL_HW_CFG = TEST_DIR + '/config/hw_cfg.json'

# upload hardware info url
# UPLOAD_HW_CFG = MES_HOST + '/hw_cfg'

# request headers
REQUEST_HEADERS = {"Content-Type": "application/json\; charset=utf-8", "x-request-datasource": "001"}



