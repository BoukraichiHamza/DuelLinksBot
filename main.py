# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyautogui
import time

middle=(997,470)
disrup_list = ['ok.png','suivant.png']

    
def find_click(filename,n):
    file = 'image/'+filename
    res = False
    button = None
    i = 0
    while (button == None) and (i<n):
        button = pyautogui.locateOnScreen(file,confidence=0.7)
        i = i+1
    pyautogui.click(button)
    if (button != None):
        res = True
    return res

def click_any(to_click):
    for f in to_click:
        find_click(f,1)

def remove_disruption():
    pyautogui.click(middle)
    click_any(disrup_list)
    
def click_wait(to_click):
    res = False
    while(not res):
        time.sleep(0.5)     
        res = click_any(to_click)
        if (not res):
            remove_disruption()

def main():
    print("Starting")
    for i in range(5):
        print(".")
        time.sleep(1)
    print("Go")
    
    #Code for aigami event (do later)
    while(True):
        click_wait(['aigami.png','aigami3.png','aigami2.png','auto.png'])
        #click_wait(['duel.png','menuskip.png','skipturn.png'])
if __name__ =="__main__":
    main()