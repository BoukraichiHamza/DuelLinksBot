# -*- coding: utf-8 -*-

import time 
import pydirectinput as di
import pyautogui
deck = "lotd/deck0.png"
oui = "lotd/oui.png"
ab = "lotd/abandon.png"

def find_place_any(L):
    print("Searching ")
    i = 0
    maxi = len(L)
    stop = False
    found = False
    while (not stop):
        print(i)
        button = pyautogui.locateOnScreen(L[i],confidence=0.7)
        if (button != None):
            pyautogui.moveTo(button)
            print(L[i]," : ",button)
            found = True
            time.sleep(0.3)
            di.press("enter")
            time.sleep(0.3)
            di.press("enter")
            time.sleep(0.3)
            di.press("left")
        i = i+1
        stop = (i > maxi - 1) or found
        print(stop)

def search(file):
    print("Searching for ",file)
    button = pyautogui.locateOnScreen(file,confidence=0.7)
    print(button)
    res = (button != None)
    if res:
        print(file,button)
        pyautogui.moveTo(button)
        time.sleep(0.3)
        di.press("enter")
    return res


print("Starting in 3s :")
for i in range(3):
    time.sleep(1)
    print(".")

while(True):
    res = search(deck)
    res = search(ab)
    if res:
        time.sleep(0.3)
        di.press("left")
        time.sleep(0.3)
        di.press("enter")
    di.press("enter")


