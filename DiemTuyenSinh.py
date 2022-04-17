class ThiSinh:
    def __init__(self, id, ten, diem, dantoc, khuvuc):
        self.id = id
        self.ten = ten
        self.diem = diem
        self.dantoc = dantoc
        self.khuvuc = khuvuc
        self.dat = ""

    def tinhdiem(self):
        if self.dantoc == "Kinh" :
            self.diem = self.diem
        else:
            self.diem += 1.5

        if self.khuvuc == 3:
            self.diem = self.diem
        elif self.khuvuc == 1:
            self.diem += 1.5
        else:
            self.diem += 1

    def xet(self):
        if self.diem < 20.5:
            self.dat = "Truot"
        else:
            self.dat = "Do"

    def __str__(self):
        return self.id + " "+ self.ten +" " + "%.1f"%self.diem +" " + self.dat

my_list = []
for i in range(int(input())):
    id = i + 1
    name = input().split()
    a = ""
    for j in name:
        a += str(j) + " "
    a = a.strip().title()
    diem = float(input())
    dantoc = input()
    khuvuc = int(input())
    my_list.append(ThiSinh("TS%02d"%id, a, diem, dantoc, khuvuc))

for i in my_list:
    i.tinhdiem()
    i.xet()

ans = sorted(my_list, key = lambda x:x.diem, reverse = True)
for i in ans:
    print(i)





