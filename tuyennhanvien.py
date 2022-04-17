class NhanVien():
    def __init__(self, ten, id, diemtb):
        self.ten = ten
        self.id = id
        self.tb = round(diemtb, 2)
        self.xh = ""

    def xephang(self):
        if self.tb < 5:
            self.xh = "TRUOT"
        elif self.tb < 8:
            self.xh = "CAN NHAC"
        elif self.tb <= 9.5:
            self.xh = "DAT"
        else:
            self.xh = "XUAT SAC"

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + ('%.2f'%self.tb) + ' ' + self.xh

my_list = []
for i in range(int(input())):
    ten = input()
    diem1 = float(input())
    diem2 = float(input())
    if diem1 > 100:
        diem1 /= 100
    elif diem1 > 10:
        diem1 /= 10
    if diem2 > 100:
        diem2 /= 100
    elif diem2 > 10:
        diem2 /= 10
    diemtb = (diem1+diem2) / 2
    id = i + 1
    my_list.append(NhanVien(ten, 'TS%02d'%id, diemtb))

for i in my_list:
    i.xephang()

ans = sorted(my_list, key = lambda x : x.tb, reverse=True)
for i in ans:
    print(i)



