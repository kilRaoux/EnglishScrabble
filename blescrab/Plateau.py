
from GameObjects.Button import *
from blescrab.Token import *


class Plateau:
    def __init__(self,scene,x,y,w,h):
        self.x,self.y,self.w,self.h = x,y,w,h
        self.dx = self.w/15
        self.dy = self.h/15
        self.dw = 50
        self.dh = 50
        self.scene = scene
        self.snb = 0
        self.nb = 0
        img =  pygame.image.load("Asset/plateau.png")
        self.fond = Button(scene,img, x=x, y=y, width=w, height=h,command=self.onClick)
        self.list_token = [[0 for i in range(15)]for j in range(15)]
        self.toDraw = []
        self.save()
        self.perks = [
            [1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1],
            [0, 3, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 3, 3],
            [0, 0, 3, 0, 0, 0, 4, 0, 4, 0, 0, 0, 3, 0, 0],
            [2, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 2],
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
            [0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0],
            [0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0],
            [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
            [0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0],
            [0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
            [2, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 2],
            [0, 0, 3, 0, 0, 0, 4, 0, 4, 0, 0, 0, 3, 0, 0],
            [0, 3, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 3, 3],
            [1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1],
        ]
    def draw(self):
        pass
    def save(self):
        self.snb = self.nb
        self.savel = [["" for i in range(15)]for j in range(15)]
        for i,l in enumerate(self.list_token):
            for j,val in enumerate(l):
                if val:
                    self.savel[i][j]=val.lettre

    def load(self):
        self.nb = self.snb
        for i,l in enumerate(self.list_token):
            for j,val in enumerate(l):
                if val:
                    val.delete()
        self.list_token = [[0 for i in range(15)]for j in range(15)]
        for i,l in enumerate(self.savel):
            for j,val in enumerate(l):
                if val!="":
                    self.addToken(val,i,j)

    def onClick(self,x,y):
        if self.scene.etat == "POSE":
            i,j = (x-self.x)//self.dx,(y-self.y)//self.dy
            if not self.addToken(self.scene.target.lettre,int(i),int(j)):
                try:
                    self.scene.target.delete()
                    if self.scene.player == 1:
                        self.scene.porteur1.list_token.remove(self.scene.target)
                        self.scene.porteur1.update()
                    if self.scene.player == 2:
                        self.scene.porteur2.list_token.remove(self.scene.target)
                        self.scene.porteur2.update()
                    self.scene.etat = 0
                    self.scene.etat = "CHOUSE"
                except:
                    print("ERREUR",self.scene.target)
    def addToken(self,token,i,j):
        if 15<i<0 or 15<j<0: return 1
        self.nb += 1
        try:
            if (self.list_token[i][j]):
                return 1
            go = Token(self.scene, token,
                       x=self.x + self.dx * i ,
                       y=self.y + self.dy * j ,
                  w=45, h=45)
            self.list_token[i][j] = go
            return 0
        except:
            return 1
    def __getitem__(self, pos):
        i,j = pos
        if 14 < i < 0 or 14 < j < 0: return 0,0
        return self.list_token[i][j],self.perks[i][j]
