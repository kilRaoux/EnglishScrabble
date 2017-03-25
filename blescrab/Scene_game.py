
import sys
from Fenetre.Scene import *
from GameObjects.Button import *
from GameObjects.EventObject import *
from GameObjects.Text import *
from blescrab import *
from blescrab.Checker import Checker
from blescrab.IA import *
from blescrab.Plateau import Plateau



class Scene_Game(Scene):
    def __init__(self,master,fMenu,w,h,dic):
        Scene.__init__(self,master)
        self.w,self.h = w,h
        self.dic = dic
        self.setTerrain("Asset/fond.png", w=w, h=h)
        Button(self, pygame.image.load("Asset/EXIT.png"), x=w - 220, y=20, width=200, height=50, command=sys.exit)
        self.porteur_joueur = Porteur(self, x=w - 800, y=h - 200, w=700, h=100,player=1)
        self.porteur_IA = Porteur(self, x=w - 800, y=100, w=700, h=100)
        [self.porteur_IA.addToken("empty") for i in range(7)]
        self.porteur_joueur.tirage()
        self.plt = Plateau(self, x=20, y=120, w=45 * 15, h=45 * 15)
        self.etat = "CHOUSE"
        self.target = ""
        self.turn = 0
        self.txt_joueur = Text(self, "Player Score: 0 ", x=800, y=300, width=100, height=20)
        self.butDraw = CheckButton(self,pygame.image.load("Asset/DRAW.png"),x=w-800,y=h-300,width=200,height=50,command_off=self.selectDraw,command_on=self.draw,
                                   image_on=pygame.image.load("Asset/Draw_on.png"))
        self.butshuffle = Button(self,pygame.image.load("Asset/SHUFFLE.png"),x = w - 300,y = h - 300, width=200,height=50,command=self.porteur_joueur.shuffle)
        self.butNext = Button(self,pygame.image.load("Asset/NEXT.png"),x = w - 550,y = h-300,width=200,height=50,command=self.next)
        self.txt_IA = Text(self, "Computer Score: 0", x=800, y=400, width=100, height=20)
        self.txt_turn = Text(self, "Turn: 0",x=800,y=500,width = 100,height=20)
        self.addCommand(self.addScore)
        self.score_joueur = 0
        self.score_IA = 0
        self.IA = IA(self.plt,self.dic)
        self.targetDraw = []
        self.setScore(0,0)
        self.words = []
        self.tour_joueur()
        self.checker = Checker(self.plt,self.dic)
    def next(self):
        if self.plt.nb == 0: return
        score = self.check()
        if score:
            self.porteur_joueur.tirage()
            self.score_joueur -= self.score_joueur - score
            self.txt_joueur.updateText("Your Score: {}".format(self.score_joueur))
            self.etat = "WAIT"
            self.tour_IA()
        else:
            self.info()
            self.porteur_joueur.load()
            self.plt.load()
    def selectDraw(self):
        if self.etat == "CHOUSE":
            self.etat = "SELECT"
    def draw(self):
        for o in self.targetDraw:
            self.porteur_joueur.list_token.remove(o)
            o.delete()
        self.targetDraw = []
        self.porteur_joueur.update()
        self.porteur_joueur.tirage()
        if self.turn:
            self.etat = "WAIT"
            self.tour_IA()
        else:
            self.etat = "CHOUSE"
    def tour_joueur(self):
        self.txt_turn.updateText("Turn: {}".format(self.turn))
        EventObject(self,pygame.image.load("Asset/YOURTURN.png"),x=0,y=0,width=self.w,height=self.h,calque=2,time = 1)
        self.porteur_joueur.save()
        self.plt.save()
        self.etat = "CHOUSE"

    def tour_IA(self):
        self.IA.myTurn()
        self.turn +=1
        self.tour_joueur()

    def addScore(self,n=0):
        self.score_joueur += n
        self.txt_joueur.updateText("Player Score:{}".format(self.score_joueur))
    def setScore(self,scoreJ,scoreIA):
        self.score_joueur = scoreJ
        self.score_IA = scoreIA
        self.txt_joueur.updateText("Player Score: {}".format(self.score_joueur))
        self.txt_IA.updateText("Computer Score: {}".format(self.score_IA))
    def check(self):
        return self.checker.check()
    def info(self):
        return
        for l in self.plt.list_token:
            for i in l:
                if i:
                    print(i.lettre,end="")
                else:
                    print(0, end="")
            print()
"""
    def _checkSingleton(self):
        try:
            for i,val in enumerate(self.plt.list_token):
                if val[0] and not self.plt.list_token[i-1][0] and not self.plt.list_token[i+1][0] and not self.plt.list_token[i][1]:
                    return 0
                elif val[-1] and not self.plt.list_token[i-1][-1] and not self.plt.list_token[i+1][-1] and not self.plt.list_token[i][-2]:
                    return 0
                elif self.plt.list_token[0][i] and not self.plt.list_token[0][i-1] and not self.plt.list_token[0][i+1] and not self.plt.list_token[1][i]:
                    return 0
                elif self.plt.list_token[-1][i] and not self.plt.list_token[-1][i-1] and not self.plt.list_token[-1][i+1] and not self.plt.list_token[-2][i]:
                    return 0
                elif not i in (0,14):
                    for j,k in enumerate(val):
                        if not j in (0,14):
                            if k and not (self.plt.list_token[i][j-1] or self.plt.list_token[i][j + 1] or self.plt.list_token[i - 1][j] or self.plt.list_token[i + 1][j]):
                                return 0
            return 1
        except: return 1

    def check(self):
        if not self.plt.list_token[7][7]: return 0
        if not self._checkSingleton(): return 0
        words = []
        score = 0
        for i,l in enumerate(self.plt.list_token):
            wordA = ""
            wordB = ""
            for j,val in enumerate(l):
                if val:
                    wordA += val.lettre
                elif wordA != "":
                    words.append(wordA)
                    wordA = ""
                if self.plt.list_token[14-i][14-j]:
                    wordB += self.plt.list_token[14-i][14-j].lettre
                elif wordB != "":
                    words.append(wordB)
                    wordB = ""
        print(words)
        cop = [["" for i in l]for l in self.plt.list_token]
        for i,l in enumerate(self.plt.list_token):
            for j,val in enumerate(l):
                if val:
                    cop[j][i] = val.lettre
        for i in cop:
            word = ""
            for j in i:
                if j:
                    word += j
                elif word != "":
                    words.append(word)
                    word = ""
        for i in words:
            if len(i) > 8: return 0
            if len(i)==1:
                words.remove(i)
            else:
                if not i in self.dic[i[0]]:
                    print("is not a word",i)
                    return 0
                if not (i in self.words):
                    self.words.append(i)
                    score += len(i)
        return score
        """
