import sys
from Windows.Scene import *
from GameObjects.Button import *


class Scene_menu(Scene):
    def __init__(self,master,w,h,fGame):
        Scene.__init__(self,master)
        Button(self, pygame.image.load("Asset/START.png"), x=w / 2 - 200, y=h / 2 - 50, width=400, height=100,
               command=fGame)
        Button(self, pygame.image.load("Asset/EXIT.png"), x=w / 2 - 200, y=h / 2 + 50, width=400, height=100,
               command=sys.exit)
        GameObject(self, pygame.image.load("Asset/blescrab.png"), x=w / 4, y=h / 10, width=int(w / 2),
                   height=int(h / 5))
        self.setTerrain("Asset/fond.png",w=w,h=h)