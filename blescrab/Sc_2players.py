
from Windows.Scene import *
from GameObjects.Button import *
from GameObjects.EventObject import *
from GameObjects.Text import *
from blescrab import *
from blescrab.Checker import Checker
from blescrab.Plateau import Plateau
from blescrab.scWin import *

class Sc_2players(Scene):
    def __init__(self,master,w,h,fmenu,dic):
        Scene.__init__(self,master)
        self.width = w
        self.height = h
        self.dic = dic
        self.setTerrain("Asset/fond.png",w=w,h=h)
        self.plt = Plateau(self, x=20, y=120, w=45 * 15, h=45 * 15)
        self.etat = "CHOUSE"
        self.player = 1
        self.target = ""
        self.targetToken = 0
        self.turn = 0
        self.checker = Checker(self.plt,self.dic)
        self.totalScore = 0
        self.arrow = GameObject(self,pygame.image.load("Asset/arrow.png"),x=w-810,y=120,width=720,height=250)
        GameObject(self,pygame.image.load("Asset/EnglishScrabble.png"),w/2-300,0,1,600,110)
        GameObject(self,pygame.image.load("Asset/token__.png"),x=w-800,y=h-270,calque=0,width=750,height=260)
        self.txtPick = Text(self,"Pick: 0",x=w-790,y=h-260,width=10,height=10,size=30)
        txt = Text(self, "Pick: 0", x=w - 790, y=h - 230, width=10, height=10, size=30)
        txt.updateText("A=1 B=3 C=3 D=2 E=1 F=4 G=2 H=4 I=1 J=8 K=5 L=1 ")
        txt = Text(self, "Pick: 0", x=w - 790, y=h - 180, width=10, height=10, size=30)
        txt.updateText("M=3 N=1 O=1 P=3 Q=10 R=1 S=1 T=1 U=1 V=4 W=4 ")
        txt = Text(self, "Pick: 0", x=w - 790, y=h - 120, width=10, height=10, size=30)
        txt.updateText("W=4 X=8 Y=4 Z=10")
        self.addCommand(self.pick)
        #Player 1
        self.porteur1 = Porteur(self,x=w - 800,y=200,w=700,h=100,player=1)
        self.score1 = 0
        self.txt1 = Text(self, "Player 1 Score: 0 ", x=w-800, y=140, width=100, height=20)
        self.txt1.updateText("Player 1 : 0")
        self.butDraw1 = CheckButton(self, pygame.image.load("Asset/DRAW.png"), x=w - 800, y=300, width=200,
                                   height=50, command_off=self.selectDraw1, command_on=self.porteur1.draw,
                                   image_on=pygame.image.load("Asset/Draw_on.png"))
        self.butshuffle1 = Button(self, pygame.image.load("Asset/SHUFFLE.png"), x=w - 300, y= 300, width=200,
                                 height=50, command=self.porteur1.shuffle)
        self.butNext1 = Button(self, pygame.image.load("Asset/NEXT.png"), x=w - 550, y=300, width=200, height=50,
                              command=self.next1)
        #Player 2
        self.porteur2 = Porteur(self, x=w - 800, y=h - 430, w=700, h=100, player=2)
        self.score2 = 0
        self.txt2 = Text(self, "Player 2 Score: 0 ", x=800, y=h-490, width=100, height=20)
        self.txt2.updateText("Player 2 : 0")
        self.butDraw2 = CheckButton(self, pygame.image.load("Asset/DRAW.png"), x=w - 800, y=h - 330, width=200,
                                      height=50, command_off=self.selectDraw2, command_on=self.porteur2.draw,
                                      image_on=pygame.image.load("Asset/Draw_on.png"))
        self.butshuffle2 = Button(self, pygame.image.load("Asset/SHUFFLE.png"), x=w - 300, y=h -330, width=200,
                                  height=50, command=self.porteur2.shuffle)
        self.butNext2 = Button(self, pygame.image.load("Asset/NEXT.png"), x=w - 550, y=h -330, width=200, height=50,
                               command=self.next2)
        self.bind("e",self.win)
        self.bind("d",self.devMod)
        self.addCommand(self.DragAndDrop)
    def pick(self):
        self.txtPick.updateText("pick: {}".format(len(self.porteur1.abc)))
    def devMod(self):
        self.devText1 = Text(self,"DevText:",0,0,100,20,10)
        self.devText2 = Text(self, "etat/player:{}/{}".format(self.etat,self.player), 0, 20, 200, 20,10)
        self.devText3 = Text(self, "DevText:", 0, 40, 100, 20,10)
        self.addCommand(self._devUpdate)
        self.bind("d", self.devModOff)
    def _devUpdate(self):
        self.devText1.updateText("DevMod True".format(self.etat, self.player))
        self.devText2.updateText("etat/player:{}/{}".format(self.etat,self.player))
        self.devText3.updateText("fps:{}".format(int(self.master.fps)))
    def devModOff(self):
        self.devText1.delete()
        self.devText2.delete()
        self.devText3.delete()
        self.lcommand.remove(self._devUpdate)
        self.bind("d", self.devMod)
    def DragAndDrop(self):
        if self.targetToken:
            x, y = pygame.mouse.get_pos()
            self.targetToken.goTo(x-20,y-20)
    def selectDraw1(self):
        if self.player == 2: return 0
        if self.etat == "CHOUSE":
            self.etat = "SELECT"
        return 1
    def selectDraw2(self):
        if self.player == 1: return 0
        if self.etat == "CHOUSE":
            self.etat = "SELECT"
        return 1
    def nextTurn(self):
        print("next turn")
        if self.player == 1:
            self.tourPlayer2()
        else:
            self.tourPlayer1()
    def next1(self,x,y):
        if self.player == 2: return
        if self.plt.nb == 0: return
        score = self.check()
        if score:
            self.porteur1.tirage()
            self.score1 += score  - self.totalScore
            self.totalScore += score - self.totalScore
            self.txt1.updateText("Player 1: {}".format(self.score1))
            self.etat = "WAIT"
            self.tourPlayer2()
        else:
            self.porteur1.load()
            self.plt.load()
    def next2(self,x,y):
        if self.player == 1: return
        if self.plt.nb == 0: return
        score = self.check()
        if score:
            self.porteur2.tirage()
            self.score2 += score - self.totalScore
            self.totalScore += score - self.totalScore
            self.txt2.updateText("Player 2: {}".format(self.score2))
            self.etat = "WAIT"
            self.tourPlayer1()
        else:
            self.porteur2.load()
            self.plt.load()
    def tourPlayer1(self):
        print(self.etat,self.player)
        self.arrow.move(0,-280)
        self.player = 1
        self.porteur1.save()
        self.plt.save()
        self.etat = "CHOUSE"
    def tourPlayer2(self):
        print(self.etat,self.player)

        self.arrow.move(0,280)
        self.player = 2
        self.porteur2.save()
        self.plt.save()
        self.etat = "CHOUSE"
    def win(self):
        self.master.setScene(ScWin(self.master,self.score1,self.score2))
    def check(self):
        return self.checker.check()
