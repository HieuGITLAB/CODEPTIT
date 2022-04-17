class SoPhuc():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def c(self, SoPhuc):
        a = self.a + SoPhuc.a
        b = self.b + SoPhuc.b
        a1 = a*self.a - b*self.b
        b1 = a*self.b + b*self.a
        return f"{a1} + {b1}i"
    def d(self, SoPhuc):
        a = self.a + SoPhuc.a
        b = self.b + SoPhuc.b
        a1 = a*a - b*b
        b1 = 2*a*b

        return f"{a1} + {b1}i" if b1 >= 0 else f"{a1} - {b1*-1}i"




t = int(input())

while t > 0:
    n = input().split()
    sp1 = SoPhuc(int(n[0]), int(n[1]))
    sp2 = SoPhuc(int(n[2]), int(n[3]))
    print(f"{sp1.c(sp2)}, {sp1.d(sp2)}")

    t -= 1