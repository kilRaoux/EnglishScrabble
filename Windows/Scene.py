import pygame
from Windows.Calque import *
from GameObjects.GameObject import *

class Scene:
    """
    Scene comptien toute les information dune phase de jeu
    """
    def __init__(self,master):
        self.master = master
        self.calque = [Calque(self), Calque(self), Calque(self)]
        self.changes = 0
        self.event = []
        self.activeItems = []
        self.clickItems = []
        self.lcommand = []
        self.dictKey = {}
        self.dictImage = {}
    def addEvent(self,event):
        self.event.append(event)
    def addCommand(self,command):
        self.lcommand.append(command)
    def bind(self,key,command):
        self.dictKey[key] = command
    def addImage(self,name,path):
        self.dictImage[name] = pygame.image.load(path)
    def addItem(self,obj,cal=-1):
        """
        Ajoute un objet au jeu pour qui soit afficher sur le plateau.
        [Warning] : doit etre de type GameObject
        :param obj: [GameObject] objet a ajouter
        :param cal: [int] numero du calque.
        """
        self.calque[cal].add(obj)
    def addActiveItem(self,obj):
        """
        Ajoute un objet a la liste active du jeu. Ainsi l'objet serra pris en compte par sa hitBox
        :param obj: [GameObject] avec hitbox
        """
        self.activeItems.append(obj)
    def delete(self,obj):
        """
        Enleve l'objet du jeu
        :param obj: [GameObject]
        :return:
        """
        self.changes = 1
        for c in self.calque:
            c.delete(obj)
        try:
            self.event.remove(obj)
        except: pass
    def loose(self,other):
        """
        Quand le jeu est perdu
        :return:
        """
        print("Perdu")
    def test(self,other):
        """
        Appel le test de colision des hitboxs des objets de la liste active
        :param other: [GameObject] de referance
        """
        for i in self.activeItems:
            i.test(other)
    def onClick(self,x,y):
        for i in self.clickItems:
            i.testClick(x,y)
    def newCalque(self):
        """
        Ajoute un calque
        """
        self.calque.append(Calque(self))
    def setTerrain(self,img,x=0,y=0,w=1080,h=1920):
        """
        Creer le terrain du jeu, ce qui correspond au fond. le terrain est toujurs sur le calque le plus bas
        :param img: image a afficher
        """
        GameObject(self, pygame.image.load(img), x, y,width=w,height=w,calque=0)#"Asset/fond.png"

