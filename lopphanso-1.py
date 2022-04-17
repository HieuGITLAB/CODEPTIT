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

arr = input().split()

phanso = PhanSo(arr[0], arr[1])
print(f"{phanso.tu//phanso.ucln()}/{phanso.mau//phanso.ucln()}")

# Tran Dinh Hieu tu lam :D