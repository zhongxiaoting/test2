import threading
import time

import threading
import time


class Itemstress():
    def run_item(self):
        for _ in range(3):
            print("the current threading 1 is running")
            time.sleep(2)
            print("the current threading 6 is running")


class ItemMem():
    def run_item(self):
        for _ in range(3):
            print("the current threading 2 is running")

            time.sleep(2)


class ItemHDD():
    def run_item(self):
        for _ in range(3):
            print("the current threading 3 is running")

            time.sleep(2)


def get_name(name):
    if name == 'ItemStress':
        return Itemstress()
    if name == 'ItemMem':
        return ItemMem()
    if name == 'ItemHDD':
        return ItemHDD()


def run_item():
    items_run = []
    items = ['ItemStress', 'ItemMem', 'ItemHDD']
    for item in items:
        items_run.append(get_name(item))
    for item_ in items_run:
        t1 = threading.Thread(target=item_.run_item)
        t1.start()

run_item()
