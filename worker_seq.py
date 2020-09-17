# -*- coding: utf-8 -*-

from threading import Thread
import pyautogui
import time


class WorkerS(Thread):

    """Worker to look for event on the screen and click"""

    def __init__(self, ListFileName):
        Thread.__init__(self,daemon=True)
        self.LFN = ListFileName
        self.die = False
        
    def find_click(self,file,n):
        res = False
        button = None
        i = 0
        while (button == None) and (i<n):
            button = pyautogui.locateOnScreen(file,confidence=0.7)
            print(button)
            i = i+1
        if (button != None):
            pyautogui.click(button)
            res = True
        return res
    
    def click_list(self):
        res = False
        for file in self.LFN :
            res_aux = self.find_click(file,1)
            res = res_aux or res
        return res
    
    def run(self):
        print('Sequential Worker Launched')
        while(not self.die):
            time.sleep(1)
            middle=(997,470)
            pyautogui.click(middle)
            res = self.click_list()
            if res :
                print("Clicked §§")
            
    def join(self):
        print("Closing Sequential Worker")
        self.die = True