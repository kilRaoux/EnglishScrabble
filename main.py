"""
------------------------------------------ English Scrabble ---------------------------------------------
Note de version:
0.0.0: MyPyGame debut.
1.0.0: Premiere version stable du jeu.
    1.0.1: hotFix
1.1.0: Ajout:
    - d'une animation au survole d'un bouton (ici dans les porteur, au survole d'un jeton pour mettre le
        avant).
    - de la gestion des cases bonus (mot compte double, triple et lettre compte double, triple).
"""



from Windows.Place import Place
from blescrab.Sc_2players import *
from blescrab.Scene_menu import Scene_menu as scm
from pygame.locals import *
__version__ = "1.1.0"


def goToGame():
    game.scene = scGame
def goToMenu():
    game.scene = scMenu
def loadDico(path="dict.txt"):
    file = open(path)
    ch = file.read()
    ch = ch.split("\n")
    dic = {"A":[],"B":[],"C":[],"D":[],"E":[],"F":[],"G":[],"H":[],"I":[],"J":[],"K":[],"L":[],"M":[],"N":[],"O":[],
           "Q":[],"R":[],"S":[],"T":[],"U":[],"V":[],"W":[],"X":[],"Y":[],"Z":[],"P":[]}
    for w in ch:
        if 1<len(w)<8:
            dic[w[0].upper()].append(w.upper())
    file.close()
    return dic

h,w = (900,1600)
game = Place(w,h)
scMenu = scm(game,w,h,goToGame)

scGame = Sc_2players(game,w,h,goToMenu,loadDico())
scGame.addImage("fond","Asset/fond.png")
game.run(scGame)
