from time import time as getTime
from GameObjects.GameObject import *

class EventObject(GameObject):
    def __init__(self,scene,image,x,y,width,height,calque=1,time=0,pause=0):
        GameObject.__init__(self,scene,image,x,y,calque,width,height)
        self.scene.addEvent(self)
        self.time = time
        self.ctime = getTime()
    def avance(self):
        if getTime()-self.ctime > self.time:
            self.delete()
