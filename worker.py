# -*- coding: utf-8 -*-


from threading import Thread
import pyautogui


class Worker(Thread):

    """Worker to look for event on the screen and click"""

    def __init__(self, FileName):
        Thread.__init__(self,daemon=True)
        self.FN = FileName
        self.die = False
        
    def find_click(self,n):
        file = self.FN
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
    
    def run(self):
        print('Worker Launched for :'+ self.FN)
        while(not self.die):
            res = self.find_click(1)
            if res :
                print(self.FN + "Clicked §§")
            
    def join(self):
        print("Closing " + self.FN)
        self.die = True
            
            