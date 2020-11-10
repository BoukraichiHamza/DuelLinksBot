# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from worker import Worker
import pyautogui
import time
import os
from queue import Queue

middle=(990,450)

def make_list(folder):
    L = []
    for filename in os.listdir(folder):
        filename = folder+"/"+filename
        #Test if new file
        Split_name = filename.split("_")
        found = False
        for f in L:
            for e in f:
                split = e.split("_")
                if split[0] == Split_name[0]:
                    found = True
            if found :
                f.append(filename)
        if not found :  
            L.append([filename])       
    return L
                    
L = make_list("event_tag")
print(L)

def main():
    WL = []
    WQ = []
    print("Starting")
    for i in range(3):
        print(".")
        time.sleep(1)
    print("Go")
    #Launch script for every image
    for e in L:
        q = Queue()
        print(e)
        w = Worker(e,q)
        w.daemon = True
        w.start()
        WL.append(w)
        WQ.append(q)
    try :  
        while(True):
            clicked = False
            for q in WQ:
                res_q = q.get()
                clicked = clicked or res_q
                print(res_q)
            if not clicked :
                pyautogui.click(middle)
                
    except KeyboardInterrupt :
        for w in WL:
            w.join()
        
if __name__ =="__main__":
    main()