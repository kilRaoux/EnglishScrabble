from Windows.Calque import Calque
from GameObjects.GameObject import *
import pygame
from pygame.locals import *
import sys
import time
FRAME_RATE = 30

class Place:
    """
    Class qui affiche la Fenetre et gére les objects et evenement
        - screen = fenetre du jeu
        - end = boolean gerant le fonctionnement de la boucle de jeu (si False le je s'arrete)
    """
    def __init__(self,width = 700,height = 700,framerate=30):
        """
        Constructeur
        :param width: largeur de la fenetre de jeu
        :param height: hauteur de la fenetre de jeu
        """
        self.width,self.height = width,height
        self.screen = pygame.display.set_mode((width,height))#,pygame.FULLSCREEN)
        self.calque = [Calque(self),Calque(self),Calque(self)]
        self.activeItems = []
        self.dictKey = {}
        self.end = 1
        self.fps = 0
        self.time = 0
        self.clock = pygame.time.Clock()
        self.framerate=framerate
    def update(self):
        """
        Met a jour le plateau
        :return:
        """
        for c in self.scene.calque:
            c.update()
        pygame.display.update()
    def blit(self,img,pos):
        """
        affiche une image sur le plateau
        :param img: image a afficher
        :param pos: turple de la position (x,y)
        :return:
        """
        self.screen.blit(img,pos)
    def action(self,key):
        self.scene.dictKey.get(key)()
    def stop(self):
        self.end = 0
    def setScene(self,scene):
        self.scene = scene
    def run(self,scene):
        self.scene = scene
        self.time = time.time()
        while 1:
            #print(self.scene)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    self.scene.onClick(x,y)
                elif event.type == 2:
                    self.action(event.unicode)
                else:
                    pass
            x,y = pygame.mouse.get_pos()
            for c in self.scene.lcommand:
                c()
            for c in self.scene.activeItems:
                c.testOver(x,y)
            self.update()
            for c in self.scene.event:
                c.avance()
            self.clock.tick(FRAME_RATE)
            self.fps = 1/(time.time() - self.time)
            self.time = time.time()
            #pygame.time.delay(int(1000/FRAME_RATE))
