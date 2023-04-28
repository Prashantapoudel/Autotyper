import time
import pyautogui as pg

for i in range(200):
    time.sleep(5)
    pg.write("hello world")
    pg.press('Enter')