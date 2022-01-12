# coding=utf-8



###############
# 1. dir and path
###############
# define test root path
TEST_DIR = '/home/test2'
STRESS_LOG = TEST_DIR + '/stress_log'
LOG_BACKUP_DIR = TEST_DIR + '/log_backup'
CFG_PATH = TEST_DIR + '/cfg.json'
RESULT_LOG_PATH = TEST_DIR + '/result.log'
FULL_LOG_PATH = TEST_DIR + '/full.log'
CONTROLLER_JSON_PATH = TEST_DIR + '/main/controller.json'
CPU_STRESS_LOG_PATH = STRESS_LOG + '/cpu_stress.log'
MEM_STRESS_LOG_PATH = STRESS_LOG + '/mem_stress.log'
HDD_STRESS_LOG_PATH = STRESS_LOG + '/hdd_stress.log'
LOSS_DISK_LOG_PATH = STRESS_LOG + '/loss_disk.log'
MCE_ECC_LOG = STRESS_LOG + '/mce_ecc.log'
STRESS_ALL_LOG = TEST_DIR + '/all_stress.log'



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