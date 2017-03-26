import random
import pygame
from GameObjects.Button import *
from GameObjects.GameObject import *
from blescrab.Token import *


class Porteur:
    def __init__(self,scene,x,y,w,h,player = 0):
        self.x,self.y,self.w,self.h = x,y,w,h
        self.dx = self.w//7
        self.dy = self.y//2
        self.dw = 50
        self.dy = 50
        self.etat = 0
        self.player = player
        self.scene = scene
        self.targetDraw = []
        self.abc = list("E"*12+"AI"*9+"O"*8+"RNT"*6+"LSU"*4+"D"*4+"G"*3+"BCMP"*2+"KJXQZ")
        if player:
            self.fond = Button(scene, pygame.image.load("Asset/porteur.png"), x=x, y=y, width=w, height=h,command=self.onClick,overCommand=self.over)
        else:
            self.fond = GameObject(scene, pygame.image.load("Asset/porteur.png"), x=x, y=y, width=w, height=h)
        self.list_token = []
        self.isSelect = [0]*7
        self.isUp = [0]*7
        self.isOver=-1
        self.tirage()
        self.save()
    def over(self,x,y,c):
        if c:
            i = int((x - self.x) // (self.w / 7))
            for j,val in enumerate(self.list_token):
                if i == j and self.isUp[i] == 0:
                    self.list_token[i].move(0,-10)
                    self.isUp[i]=1
                    self.isOver = i
                elif i != j and self.isUp[j] == 1:
                    self.list_token[j].move(0, 10)
                    self.isUp[j] = 0
        else:
            for i,val in enumerate(self.isUp):
                if val:
                    self.isUp[i]=0
                    self.list_token[i].move(0,10)
                self.isOver = -1
    def draw(self):
        print(self.player,self.scene.etat)
        for o in self.targetDraw:
            self.list_token.remove(o)
            o.delete()
        self.targetDraw = []
        self.update()
        self.tirage()
        self.etat = "WAIT"
        self.scene.nextTurn()

        print(self.player,self.scene.etat)
    def shuffle(self,x,y):
        save = [t.lettre for t in self.list_token]
        random.shuffle(save)
        for k in self.list_token:
            k.delete()
        self.list_token = []
        for s in save:
            self.addToken(s)
        self.update()
    def save(self):
        self.savel = [i.lettre for i in self.list_token[:]]
    def load(self):
        for i in self.list_token:
            i.delete()
        self.list_token = []

        for s in self.savel:
            self.addToken(s)
        self.scene.target = 0
        self.scene.etat = "CHOUSE"
        self.update()
    def onClick(self,x,y):
        if self.scene.player == self.player:
            if self.scene.etat == "SELECT":
                i = int((x - self.x) // (self.w / 7))
                if not self.isSelect[i]:
                    self.targetDraw.append(self.list_token[i])
                    self.list_token[i].move(0,-10)
                    self.isSelect[i] = 1
                else:
                    self.targetDraw.remove(self.list_token[i])
                    self.list_token[i].move(0,10)
                    self.isSelect[i] = 0
            elif self.scene.etat == "CHOUSE":
                x, y = pygame.mouse.get_pos()
                i = int((x - self.x) // (self.w / 7))
                if i>=len(self.list_token): return
                self.scene.target = self.list_token[i]
                self.list_token[i].move(0,-10)
                self.scene.etat = "POSE"
            elif self.scene.etat == "POSE":
                x, y = pygame.mouse.get_pos()
                i = int((x - self.x) // (self.w / 7))
                if i>=len(self.list_token): return
                if self.scene.target == self.list_token[i]:
                    self.list_token[i].move(0,10)
                    self.scene.etat = "CHOUSE"
            else:
                print(self.scene.etat)
        else:
            print(self.player)
    def addToken(self,token):
        go = Token(self.scene,token,
                        x= self.x+self.dx*len(self.list_token)+10,y = self.y+10,
                        w=80,h=80)
        self.list_token.append(go)
    def update(self):
        save = ""
        for i in self.list_token:
            i.delete()
            save += i.lettre
        self.list_token = []
        for s in save:
            self.addToken(s)
    def tirage(self):
        self.isSelect = [0]*7
        for i in range(7-len(self.list_token)):
            random.shuffle(self.abc)
            self.addToken(self.abc[0])
            self.abc.remove(self.abc[0])

