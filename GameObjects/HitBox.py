class HitBox_Rectangle:
    def __init__(self,x,y,w,h,command):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.command = command
        print(self.x-w/2,self.y-h/2)
    def test(self,other):
        x,y = other.get_pos()
        if self.x-self.w/2 < x < self.x+self.w/2 and self.y-self.h/2 < y < self.y+self.h/2:
            self.run(other)
    def run(self,other):
            self.command(other)

class HitBox_Cercle:
    def __init__(self,x,y,r,command):
        self.x,self.y = x,y
        self.r = r
        self.command = command
    def test(self,other):
        x = self.x + other.x
        y = self.y + other.y
        if x**2+y**2 < self.r:
            self.run(other)
    def run(self,**kwargs):
        self.command(**kwargs)