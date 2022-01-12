# coding=utf-8
import json,sys
sys.path.append("..")
import requests as r
from utils import times as t,log as l,handle as h
from config import constants as c
import controller as ctrl

class Item(object):

    def __init__(self):
        # self.t_pass = Fail
        self.result_json = {}
        # self.info = {}
        

    def run(self):
        self.run_item()
        return

    # child class must implement the method
    def run_item(self):
        raise NotImplementedError

    # write result our need show info 
    def set_json(self,k,v):
        self.result_json[k] = v

    # check mes status
    def check_mes_connect(self):
        response =r.Request().get(c.MES_HOST)
        if response:
            print(response)
    # test pass
    def result_pass(self):
        l.title_item(self.info['name']+ ' PASS ')
        
    # test fail
    def result_fail(self):
        l.fail_msg(self.info['name']+ ' Fail')
        ctrl.Controller.pasue()
        return 

    # cmd check
    def run_cmd(self, cmd):
        data =h.run_cmd(cmd)
        if data:
            return data
        return data

