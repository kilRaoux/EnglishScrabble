from GameObjects.GameObject import *
def empty(x,y,c):pass
class Button(GameObject):
    def __init__(self,scene,image,x,y,
                 width = 0,height = 0,
                 command = None,overCommand = empty):
        GameObject.__init__(self,scene,image,x,y,calque=1,width=width,height=height)
        self.w,self.h = width,height
        self.command = command
        self.overCommand = overCommand
        self.scene.activeItems.append(self)
        scene.clickItems.append(self)
    def testClick(self,x,y):
        if self.x < x < self.x+self.w and self.y < y < self.y+self.h:
            try:self.command(x,y)
            except: self.command()
    def testOver(self,x,y):
        self.overCommand(x,y,self.x < x < self.x+self.w and self.y < y < self.y+self.h)
class CheckButton(Button):
    def __init__(self, scene, image, x, y,
                 width=0, height=0,
                 command_on=None,command_off = None,image_on=None):
        GameObject.__init__(self, scene, image, x, y, calque=1, width=width, height=height)
        self.w, self.h = width, height
        scene.clickItems.append(self)
        self.image_on = image_on
        self.cmd_on,self.cmd_off=command_on,command_off
        self.image_off = image
        self.etat = 0
    def testClick(self,x,y):
        if self.x < x < self.x+self.w and self.y < y < self.y+self.h:
            if self.etat:
                self.etat = 0
                self.setImage(self.image_off)
                self.cmd_on()
            elif self.scene.etat == "CHOUSE":
                self.etat = 1
                self.setImage(self.image_on)
                self.cmd_off()