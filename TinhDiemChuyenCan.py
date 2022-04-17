class SinhVien():
    def __init__(self, masv, ten, lop):
        self.masv = masv
        self.ten = ten
        self.lop = lop
        self.diem = 10
        self.dg = ""
    def xuli(self, dg):
        self.diem = self.diem - (dg.count("m")*1 + dg.count("v")*2)
        if self.diem < 0:
            self.diem = 0
        if self.diem == 0:
            self.dg = "KDDK"

    def __str__(self):
        if self.diem != 0:
            return self.masv + ' ' + self.ten + ' ' + self.lop + ' ' + '%.0f'%self.diem
        else:
            return self.masv + ' ' + self.ten + ' ' + self.lop + ' ' + '%.0f'%self.diem + ' ' + self.dg


my_list = []
t = k = int(input())

while t > 0:
    masv = input()
    ten = input()
    lop = input()
    my_list.append(SinhVien(masv, ten, lop))
    t -= 1

while k > 0:
    dg = input().split()
    for i in my_list:
        if i.masv == dg[0]:
            i.xuli(dg[1])
    k -= 1
for i in my_list:
    print(i)