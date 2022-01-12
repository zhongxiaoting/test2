import sys,time
sys.path.append("..")
from main.item import Item

class ELECTRONIC_TAG_CHECK(Item):
    def __init__(self,info):
        self.info = info
        print('ELECTRONIC-TAG-CHECK')
        
    def run_item(self):
        time.sleep(5)
        self.result_pass()