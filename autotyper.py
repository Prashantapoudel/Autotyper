#Writing a python code that autotypes something that has been on program and press enter automatically.
# it types at the curser blinking.


#importing the necessary library and modules.


import time #imorting time to know the sleep time
#importing pyautogui for the mouse point and pressing enter.
import pyautogui as pg #shortening the pyautogui as pg

for i in range(200): #Starting the loop for how many times you want to print that.
    time.sleep(5)# waiting time after typing
    pg.write("hello world")# text you want to type
    pg.press('Enter') # does the work of enter button on keyboard and ready for another text after 5 sec
