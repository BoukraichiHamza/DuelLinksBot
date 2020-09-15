# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from worker import Worker
import pyautogui
import time

middle=(997,470)
disrup_list = ['ok.png','suivant.png']
click_list = ['menuskip.png','skipturn.png','duel.png']

L = click_list + disrup_list
WL = []

def main():
    print("Starting")
    for i in range(3):
        print(".")
        time.sleep(1)
    print("Go")
    #Launch script for every image
    for e in L:
        print(e)
        w = Worker('image/'+e)
        w.daemon = True
        w.start()
        WL.append(w)
    try :  
        while(True):
            time.sleep(5)
            pyautogui.click(middle)
    except KeyboardInterrupt :
        for w in WL:
            w.join()
    # while(True):
    #     time.sleep(1)
        
if __name__ =="__main__":
    main()