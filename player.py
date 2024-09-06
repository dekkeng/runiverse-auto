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
        self.titanium = self.getPos("titanium")
        self.diamond = self.getPos("diamond")
        self.select = self.getPos("select")
        self.profile = self.getPos("profile")
    
    def checkClick(self, type):        
        pos = self.getPos(type)
        if pos != None:
            self.key('1')
            self.click(pos)
            self.move([10,10])
            return True
        else:  
            return False
        
    def autoAttack(self):
        #self.log("Check screen...")
        #self.move([1,1])
        #self.updatePos()
        self.wait(1)
        if self.checkClick("skill4"):
            return True
        elif self.checkClick("skill3"):
            return True
        elif self.checkClick("skill2"):
            return True
        elif self.checkClick("skill1"):
            return True
        elif self.checkClick("diamond"):
            return True
        elif self.checkClick("titanium"):
            return True
        elif self.checkClick("continue"):
            return True
        # elif self.checkClick("continue2"):
        #   return True
        elif self.checkClick("select"):
            return True
        elif self.getPos("profile") != None:
            self.walk()

    def getPos(self, file, conf = 0.9):
        return pyautogui.locateCenterOnScreen('./sample/'+file+'.png', confidence = conf, grayscale=True)

    def getAllPos(self, file, conf = 0.7):
        return pyautogui.locateAllOnScreen('./sample/'+file+'.png', confidence = conf, grayscale=True)

    def wait(self, length = 0.01):
        sleep(length)
    def move(self, pos):
        pyautogui.moveTo(pos, duration=0.01)
        
    def key(self, key):
        if self.WALK_MAX_DURATION > 0:
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
