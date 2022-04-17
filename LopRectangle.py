class Rectangle():
    def __init__(self, cd, cr, color):
        self.cd = cd
        self.cr = cr
        self.color = color
    def dientich(self):
        return self.cd * self.cr

    def chuvi(self):
        return (self.cd + self.cr) * 2

    def mausac(self):
        return self.color.title()

n = input().split()
if int(n[0]) <= 0 or int(n[1]) <= 0:
    print("INVALID")
else:
    r = Rectangle(int(n[0]), int(n[1]), n[2])
    print(f"{r.chuvi()} {r.dientich()} {r.mausac()}")


s = input()
str