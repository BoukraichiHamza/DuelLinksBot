# -*- coding: utf-8 -*-

import pyautogui
import time
import keyboard
import os

L = []
for filename in os.listdir("lotd"):
    L.append("lotd/"+filename)
    
def find_click(file,n):
    res = False
    button = None
    i = 0
    while (button == None) and (i<n):
        button = pyautogui.locateOnScreen(file,confidence=0.7)
        print(button)
        i = i+1
    if (button != None):
        pyautogui.click(button)
        for j in range(10):
            pyautogui.press("enter")
        res = True
    return res

def click_list(L):
    res = False
    for file in L :
        res_aux = find_click(file,1)
        res = res_aux or res
    return res


print('Starting')
for i in range(3):
    time.sleep(1)
    print(".")

loop = True
while(loop):
    click_list(L)
    loop = not keyboard.is_pressed('q')
    