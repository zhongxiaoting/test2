# coding=utf-8
import os,sys,json,commands
import log as l
sys.path.append("..")
from config import constants as c

# read config info
def read_cfg(dir):
    return json.load(open(dir))

# scan sn number
def scan_sn():
    sn = ''
    while True:
        sn = raw_input('Please scan SN number:')
        if len(sn) < c.SN_MINI_NUMBER:
            l.fail_msg("SN number too short, Please retry!")
            continue
        else:
            l.log("Scan sn is: " + sn, 0 ,True)
            break
    return sn
    

# input operator number
def operator():
    operator = ''
    while True:
        operator = raw_input('Please input operator number:')
        if len(operator) < c.OPERATOR_MINI_NUMBER:
            l.fail_msg("SN number too short, Please retry!")
            continue
        else:
            # self.ctrl['OPERATOR'] = self.operator
            l.log("Input operator is: " + operator, 0 ,True)
            break
    return operator

# update controller info 
def update_controller_json(cfg):
    f = open(c.CONTROLLER_JSON_PATH,'w')
    json.dump(cfg,f)
    f.close()




# define run cmd in system
def run_cmd(cmd, w=False):
    statusoutput = commands.getstatusoutput(cmd)
    # l.write_debug_log("[command: " + cmd + "]" + '\n')
    # l.log("[command: " + cmd + "]", 0 ,w)
    if statusoutput[0] != 0:
        # l.fail_msg("[command: " + cmd + "]"+ "Fail!")
        # return None
        fail_msg = "[command: " + cmd + "]" + " Fail!"
        return fail_msg
    else:
        # 有可能发送命令成功，但是是设定命令，没有返回值
        if statusoutput[1]:
            return statusoutput[1]
        return None
