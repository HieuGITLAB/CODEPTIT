class SinhVien():
    def __init__(self, name, diem, id):
        self.name = name
        self.diem = diem
        self.id = id
        self.xh = ""
        self.tb = 0

    def tinhdiem(self):
        sum = dem = 0
        for i in self.diem:
            if dem <= 1:
                sum += (i * 2)
            else:
                sum += i
            dem += 1
        self.tb = round(sum/10/1.2, 1)

    def xephang(self):
        if self. tb >= 9:
            self.xh = "XUAT SAC"
        elif self.tb >= 8:
            self.xh = "GIOI"
        elif self.tb >= 7:
            self.xh = "KHA"
        elif self.tb >= 5:
            self.xh = "TB"
        else:
            self.xh = "YEU"

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + ('%.1f'%self.tb) + ' ' + self.xh


my_list = []
for i in range(int(input())):
    ten = input()
    diem = [float(i) for i in input().split()]
    id = i + 1
    my_list.append(SinhVien(ten, diem, 'HS%02d'%id))

for i in my_list:
    i.tinhdiem()
    i.xephang()
    print(i)
ans = sorted(my_list, key = lambda x: x.tb, reverse=True)
for i in ans:
    print(i)


