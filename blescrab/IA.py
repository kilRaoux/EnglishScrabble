import random
class IA:
    def __init__(self,plt,dic):
        self.plt = plt
        self.dic = dic
        self.buildRef()
        self.score = 0
        self.c=[(1,0),(-1,0),(0,1),(0,-1)]
    def myTurn(self,m=20):
        if not m: return
        self.plt.save()
        s,i,j = self.chouse()
        n,c = self.check(i,j)
        if not n or not c: return self.myTurn(m-1)
        w = self.find(s,n)
        if not w:return self.myTurn(m-1)
        self.play(w,i,j,c)
        chec = self.plt.scene.check()
        if chec:
            self.score += chec
            self.plt.scene.txt_IA.updateText("IA Score {}".format(self.score))
            self.plt.scene.score_IA += len(w)
        else:
            self.plt.scene.info()
            self.plt.load()
            self.myTurn(m-1)
            return


    def play(self,w,i,j,c):
        if not c: return
        i += c[0]
        j += c[1]
        for s in w[1:]:
            self.plt.addToken(s,i,j)
            i += c[0]
            j += c[1]
    def checkPlace(self,i,j,c):
        if 15>i-c[0]>0 and 15>j-c[1]>0 and self.plt.list_token[i-c[0]][j-c[1]]: return 0
        i += c[0]
        j += c[1]
        n = 0
        while 15>i>=0 and 15>j>=0 and not self.plt.list_token[i][j]:
            i += c[0]
            j += c[1]
            n += 1
        return min(n,7)

    def check(self,i,j):
        c = self.c
        random.shuffle(c)
        for k in c:
            n = self.checkPlace(i,j,k)
            if n: return n,k
        return 0,0
    def buildRef(self):
        res = []
        for i,l in enumerate(self.plt.list_token):
            for j,val in enumerate(l):
                if val:
                    res.append((val.lettre,i,j))
        return res
    def find(self,s,n):
        i = 40
        while i:
            i-=1
            w = random.choice(self.dic[s])
            if len(s) <= n: return w.upper()
        return 0
    def chouse(self):
        ch = self.buildRef()
        if not ch:
            return 0,0,0
        else:
            return ch[random.randint(0,len(ch)-1)]
