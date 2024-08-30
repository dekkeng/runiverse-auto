import os, pyautogui
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
import random

#pyautogui.PAUSE=0

load_dotenv("config.txt")

class Player:
    def __init__(self):        
        self.WALK_MAX_DURATION = float(os.getenv('WALK_MAX_DURATION', 2))
        self.updatePos()

    def updatePos(self):
        self.cont = self.getPos("continue")
        self.cont2 = self.getPos("continue2")
        self.skill1 = self.getPos("skill1")
        self.skill2 = self.getPos("skill2")
        self.skill3 = self.getPos("skill3")
        self.skill4 = self.getPos("skill4")
        self.diamond = self.getPos("diamond")
        
    def autoAttack(self):
        #self.log("Check screen...")
        #self.move([1,1])
        self.updatePos()
        if self.skill4 != None:
            self.click(self.skill4)
        elif self.skill3 != None:
            self.click(self.skill3)
        elif self.skill2 != None:
            self.click(self.skill2)
        elif self.skill1 != None:
            self.click(self.skill1)
        elif self.diamond != None:
            self.click(self.diamond)
        elif self.cont != None:
            self.log("CONTINUE")
            self.click(self.cont)
            self.wait(5)
        elif self.cont2 != None:
            self.log("CONTINUE2")
            self.click(self.cont2)
            self.wait(5)
        else:
            self.walk()
        self.move([10,10])
        self.wait(1)

    def getPos(self, file, conf = 0.9):
        return pyautogui.locateCenterOnScreen('./sample/'+file+'.png', confidence = conf)

    def getAllPos(self, file, conf = 0.7):
        return pyautogui.locateAllOnScreen('./sample/'+file+'.png', confidence = conf)

    def wait(self, length = 0.01):
        sleep(length)
    def move(self, pos):
        pyautogui.moveTo(pos, duration=0.01)
        
    def key(self, key):
        pyautogui.keyDown(key)
        self.wait(random.uniform(0,self.WALK_MAX_DURATION))
        pyautogui.keyUp(key)
        
    def walk(self):
        self.key('A')
        self.key('W')
        self.key('D')
        self.key('S')

    def drag(self, pos1, pos2):
        pyautogui.mouseDown(pos1, duration=0.01)
        pyautogui.dragTo(pos2, duration=0.2)
        pyautogui.mouseUp(pos2, duration=0.01)
        
    def click(self, pos):
        self.move(pos)
        pyautogui.click([pos[0], pos[1]])
        
    def log(self, msg):
        """Msg log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')
