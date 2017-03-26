class Checker:
    def __init__(self,plt,dic):
        self.plt = plt
        self.dic = dic
        self.list = []
    def check(self):
        if not self.plt[7,7][0]:
            print("None on 77")
            return 0
        if not self._single():
            print("single")
            return 0
        self._LR()
        score = self._checkWords()
        self.list = []
        return score
    def _checkWords(self):
        def reverse(w):
            res = ""
            for s in w:
                res = s + res
            return res
        score = 0
        for w in self.list:
            if w[0] != "" and len(w[0])>1:
                rw = reverse(w[0])
                if w[0] in self.dic[w[0][0]] or rw in self.dic[rw[0][0]]:
                    score += w[1]
                else:
                    print("BAD",)
                    return 0
        return score
    def _LR(self):
        wL,wR = "",""
        sL,sR = 0,0
        uL,uR = 1,1
        for i in range(15):
            for j in range(15):
                if self.plt[i,j][0]:
                    w,k = self.plt[i,j]
                    wL += w.lettre
                    if k == 1: uL *= 3
                    elif k == 2: sL += w.val
                    elif k == 3: sL += w.val*2
                    elif k == 4: uL *= 2
                    sL += w.val
                elif wL != "" and len(wL):
                    self.list.append((wL,sL*uL))
                    wL,sL,uL = "",0,1
                if self.plt[j, i][0]:
                    w, k = self.plt[j, i]
                    wR += w.lettre
                    if k == 1:
                        uR *= 3
                    elif k == 2:
                        sR += w.val
                    elif k == 3:
                        sR += w.val * 2
                    elif k == 4:
                        uR *= 2
                    sR += w.val
                elif wR != "" and len(wR):
                    self.list.append((wR, sR * uR))
                    wR, sR, uR = "", 0, 1
        #print(self.list)
    def _single(self):
        for i in range(14):
            for j in range(14):
                if self.plt[i,j][0] and not (self.plt[i - 1,j][0] or self.plt[i + 1,j][0] or self.plt[i,j - 1][0] or self.plt[i,j + 1][0]):
                    return 0
        return 1
