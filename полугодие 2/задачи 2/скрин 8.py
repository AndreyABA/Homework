import math
class tochka:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def zxc(self, wasd):
        return math.sqrt((self.x-wasd.x)**2 + (self.y-wasd.y)**2)
    def move(self, dx, dy):
        self.x+=dx
        self.y+=dy
    def na_osi(self):
        return self.x==0 or self.y==0
a=tochka(0, 0)
b=tochka(3, 4)
print(a.zxc(b))
a.move(1, 2)
print(a.x, a.y)
print(a.na_osi())
print(b.na_osi())
c=tochka(0, 5)
print(c.na_osi())