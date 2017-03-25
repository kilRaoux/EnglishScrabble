from Windows.Scene import Scene
from GameObjects.GameObject import *
from GameObjects.Button import Button
from Windows.Place import Place
import pygame
import sys
class ScWin(Scene):
    def __init__(self,game,p1=0,p2=0):
        Scene.__init__(self,game)
        self.master.setScene(self)
        self.bind("e", sys.exit)
        self.p1 = p1
        self.p2 = p2
        w = self.master.width
        Button(self,pygame.image.load("Asset/fond.png"),0,0,self.master.width,self.master.height,command=sys.exit)

        if p1 > p2:
            GameObject(self,pygame.image.load("Asset/win1.png"),w/2-500,100,1,width=1000,height=400)
        else:
            GameObject(self, pygame.image.load("Asset/win2.png"), w / 2 - 500, 100, 1, width=1000, height=400)

if __name__ == "__main__":
    game = Place()
    sc = ScWin(game,88,100)
    print("hey")
    game.run(sc)