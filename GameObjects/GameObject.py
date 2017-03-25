import pygame as pg
from GameObjects.HitBox import *
class GameObject:
    """
    Objet d'affichage du jeu.
    Tout ce qui doit etre afficher doit heriter de cette classe
    """
    def __init__(self,scene,image,x,y,calque = 1,width = 0,height = 0):
        """
        Constructeur
        :param scene: scene ou l'obj va etre afficher
        :param image: str ou pygame.surface:
            - si str: creer une image de lien, ici image donne le lien de l'image
            - si surface: si on veut un autre type de surface
        :param x: position sur x. [Attention] L'anchor le point en haut a gauche.
        :param y: position sur y. [Attention] L'anchor le point en haut a gauche.
        :param calque: numero du calque d'affichage. Nombre entier positif.
        :param width: largeur du composant image.
        :param height: hauteur du composant image.
        """
        # Affectation des variables.
        self.scene = scene
        self.master = scene.master
        self.x, self.y = x, y
        self.width, self.height = width, height

        # Gestion du type (si str ou pygame.surface)
        if type(image) == str:
            self.image = 0
        else:
            self.image = image

        # Gestion de la largeur et hauteur de l'image
        self.scale(width,height)

        # Autre
        self.scene.addItem(self,calque) # Ajout a la liste des objs a afficher de la scene
        self.scene.changes = 1
        self.pos = image.get_rect().move(x, y) # \* UNKNOWN *\

    def setImage(self,img):
        """
        Permet de changer L'image
        :param img: pygame.surface de la nouvelle image
        :return: None
        """
        self.scene.changes = 1
        self.image = img
        self.scale(self.w,self.h)
    def delete(self):
        """
        Suprime l'affichage de l'obj
        :return: None
        """
        self.scene.delete(self)
    def goTo(self,x,y):
        """
        Bouge l'obj a la posion x,y
        :param x: nombre
        :param y: nombre
        :return: None
        """
        dx = x - self.x
        dy = y - self.y
        self._move(dx,dy)
    def move(self,dx,dy):
        """
        Bouge l'obj de dx,dy
        Peut etre OverRide a l'heritage
        :param dx: deplacement sur x
        :param dy: deplacement sur y
        :return: None
        """
        self._move(dx,dy)
    def _move(self,dx,dy):
        """
        [Attention] Methode priver, a ne pas OverRide
        :param dx: deplacement sur x
        :param dy: deplacement sur y
        :return: None
        """
        self.scene.changes = 1
        self.x += dx
        self.y += dy
        self.pos = self.pos.move(int(dx),int(dy))
    def scale(self,width,height):
        """
        Change la taille du composant
        :param width: nouvelle largeur
        :param h: nouvelle hauteur
        :return: None
        """
        self.width,self.height = width,height
        self.image = pg.transform.scale(self.image, (width,height))
    def update(self):
        """
        Met a jour l'affichage du composant
        :return: None
        """
        self.master.blit(self.image,self.get_pos())
    def get_pos(self):
        """
        Donne la position de l'obj
        :return: position sur x et position sur y
        """
        return self.x,self.y
    def get_size(self):
        return self.image.get_width(),self.image.get_height

