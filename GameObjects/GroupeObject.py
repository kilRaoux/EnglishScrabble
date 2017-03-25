from GameObjects.GameObject import *

class GroupeObject:
    def __init__(self,scene):
        self.master = scene.master
        self.scene = scene
        self.objects = []
    def get_pos(self,i=0):
        x = self.objects[0].x
        y = self.objects[0].y
        return x,y
    def update(self):
        for o in self.objects:
            o.update()
    def addObject(self,obj):
        self.objects.append(obj)
    def scale(self,w,h,i="ALL"):
        if i == "ALL":
            for o in self.objects:
                o.scale(w,h)
        else:
            self.objects[i].scale(w,h)
    def move(self,dx,dy):
        for o in self.objects:
            o.move(dx,dy)