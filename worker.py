# -*- coding: utf-8 -*-


from threading import Thread
import pyautogui
import time
from queue import Queue
middle=(997,470)
class Worker(Thread):

    """Worker to look for event on the screen and click"""

    def __init__(self, FileList,q):
        Thread.__init__(self,daemon=True)
        self.FL = FileList
        self.die = False
        self.q = q
        
    def find_click(self,file,n):
        file = file
        res = False
        button = None
        i = 0
        while (button == None) and (i<n):
            button = pyautogui.locateOnScreen(file,confidence=0.7)
            i = i+1
            print(button)
        if (button != None):
            res = True
            print(button)
            pyautogui.click(button)
        return res
    
    def run(self):
        print('Worker Launched for :', self.FL)
        while(not self.die):
            res = False
            for file in self.FL:
                print("Looking for :",file)
                resaux = self.find_click(file,1)
                res = res and resaux
                time.sleep(0.1)
            self.q.put(res)
            if res :
                print("Clicked §§",self.FL)
            
            
    def join(self):
        print("Closing ", self.FL)
        self.die = True
            
            