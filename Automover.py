import pyautogui as pag
import random
import time
while True:
    x = random.randint(600,700)
    y = random.randint(200,400)
    pag.moveTo(x,y,0.5)
    time.sleep(2)
    
