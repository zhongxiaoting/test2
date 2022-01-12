import sys,time
sys.path.append("..")
from main.item import Item

class FW_CHECK(Item):
    def __init__(self,info):
        self.info = info
        print('FW-CHECK')
        
    def run_item(self):
        time.sleep(5)
        self.result_pass()