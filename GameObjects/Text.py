import pygame
from GameObjects.GameObject import *


class Text(GameObject):
    def __init__(self,scene,text,x,y,width,height):
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsansms",50)
        txt = self.font.render(text,1,(0,0,0))
        GameObject.__init__(self,scene,txt,x=x,y=y,width=width,height=height)
    def updateText(self,txt):
        self.image = self.font.render(txt,1,(0,0,0))