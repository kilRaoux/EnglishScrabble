import pygame
from GameObjects.GameObject import *


class Text(GameObject):
    def __init__(self,scene,text,x,y,width,height,size=50):
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsansms",size)
        txt = self.font.render(text,1,(0,0,0))
        GameObject.__init__(self,scene,txt,x=x,y=y,width=width,height=height)
        self.color = (0,0,0)
    def updateText(self,txt):
        self.txt = txt
        self.image = self.font.render(self.txt,1,self.color)
    def setColor(self,r,g,b):
        self.color = (r,g,b)
        self.image = self.font.render(self.txt, 1, self.color)