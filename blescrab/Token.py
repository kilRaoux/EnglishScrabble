import pygame
from GameObjects.GameObject import *


class Token(GameObject):
    d = {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,"O":1,
         "P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}
    def __init__(self,scene,lettre,x,y,w,h):
        GameObject.__init__(self,scene,pygame.image.load("Asset/tokens/{}.png".format(lettre)),x,y,width=w,height=h)
        self.lettre = lettre
        self.val = self.__class__.d[lettre]
    def __str__(self):
        return self.lettre