class PhanSo():
    def __init__(self, tu, mau):
        self.tu = int(tu)
        self.mau = int(mau)

    def ucln(self):
        a = self.tu
        b = self.mau
        while b != 0:
            x = a % b
            a, b = b, x
        return a
    def Tu(self, PhanSo):
        return self.tu * PhanSo.mau + self.mau * PhanSo.tu

    def Mau(self, PhanSo):
        return self.mau * PhanSo.mau


def ucln(a, b):
    while b != 0:
        x = a % b
        a, b = b, x
    return a

arr = input().split()
ps1 = PhanSo(arr[0], arr[1])
ps2 = PhanSo(arr[2], arr[3])
tu = ps1.Tu(ps2)
mau = ps1.Mau(ps2)
print(f"{tu//ucln(tu, mau)}/{mau//ucln(tu, mau)}")




