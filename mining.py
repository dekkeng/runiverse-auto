import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from time import sleep
import os, random
from dotenv import load_dotenv

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://game.runiverse.world/")
webWait = WebDriverWait(driver, timeout=5)

load_dotenv("config.txt")

RUNIVERSE_USER = os.getenv('RUNIVERSE_USER', '')
RUNIVERSE_PASS = os.getenv('RUNIVERSE_PASS', '')
WAIT_LOGIN_LOADING = float(os.getenv('WAIT_LOGIN_LOADING', 30))
WALK_MAX_DURATION = float(os.getenv('WALK_MAX_DURATION', 2))
MINING_AUTO_ATTACK = float(os.getenv('MINING_AUTO_ATTACK', 0))

print("Start Runiverse Mining!")

def wait(length = 0.01):
    sleep(length)

def log(msg):
    """Msg log"""
    t = datetime.now().strftime('%H:%M:%S')
    print(f'[{t}] MESSAGE: {msg}')

def click(element):
    driver.execute_script("arguments[0].click();", element)

def key(key, delay = 0):    
    #log("Key..."+key)
    actions = ActionChains(driver)
    actions.key_down(key)
    actions.pause(delay)
    actions.key_up(key)
    actions.perform()

def initial():
    log("Checking...")    
    login_email = driver.find_element(By.ID, 'email')
    login_pass = driver.find_element(By.ID, 'password')
    if login_email.is_displayed() and login_pass.is_displayed():
        log("Logging in...")
        login_email.send_keys(RUNIVERSE_USER)
        wait(0.5)
        login_pass.send_keys(RUNIVERSE_PASS)
        wait(0.5)
        key(Keys.ENTER)
        wait(WAIT_LOGIN_LOADING)
        key(Keys.ENTER)
        wait(WAIT_LOGIN_LOADING)

def walk():
    if WALK_MAX_DURATION > 0:
        dir = random.choice(['A', 'W', 'D', 'S'])
        key(dir, random.uniform(0,WALK_MAX_DURATION))
    key('e')

# def check():
#     char_btn = driver.find_element(By.XPATH, "//img[@src='{}']".format('../images/UI/Container/Hud/Button_Character_Sheet.png'))
#     if char_btn.is_displayed():
#         walk()
#     else:
#         key('4')
#         wait(0.5)
#         key('3')
#         wait(0.5)
#         key('2')
#         wait(0.5)
#         key('1')
#         wait(0.5)
#    wait(1)

def check():
    walk()
    if MINING_AUTO_ATTACK > 0:
        key('4')
        wait(0.5)
        key('3')
        wait(0.5)
        key('2')
        wait(0.5)
        key('1')
        wait(0.5)
    wait(1)

try:
    initial()
    while True:
        check()
except Exception as e:
    log(e)
    pass

