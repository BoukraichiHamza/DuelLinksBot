# -*- coding: utf-8 -*-
from worker_seq import WorkerS
import pyautogui
import time
import os

L = []
for filename in os.listdir("image"):
    L.append("image/"+filename)
WL = []


print("Starting")
for i in range(3):
    print(".")
    time.sleep(1)
print("Go")
#Launch script for every image

w = WorkerS(L)
w.daemon = True
w.start()
WL.append(w)
try :  
    while(True):
        time.sleep(1)
        #pyautogui.press("enter")
except KeyboardInterrupt :
    for w in WL:
        w.join()
