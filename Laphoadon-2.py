import  datetime

class KhachHang():
    def __init__(self, id, ten, phong, day1, day2, phuphi):
        self.id = id
        self.ten = ten
        self.phong = phong
        self.day1 = day1
        self.day2 = day2
        self.ngayo = 0
        self.phuphi = phuphi
        self.chiphi = 0

    def xuli(self):
        pday1 = datetime.datetime.strptime(self.day1, "%d/%m/%Y")
        pday2 = datetime.datetime.strptime(self.day2, "%d/%m/%Y")
        self.ngayo = int((pday2 - pday1).days) + 1
        tang = self.phong // 100
        if tang == 1:
            self.chiphi = (self.ngayo*25) + self.phuphi
        elif tang == 2:
            self.chiphi = (self.ngayo*34) + self.phuphi
        elif tang == 3:
            self.chiphi = (self.ngayo*50) + self.phuphi
        else:
            self.chiphi = (self.ngayo*80) + self.phuphi

    def __str__(self):
        return self.id + " " + self.ten + " " + "%.0f"%self.phong + " " + "%.0f"%self.ngayo + " " + "%.0f"%self.chiphi



my_list = []
for i in range(int(input())):
    ten = input().strip()
    phong = int(input())
    day1 = input().strip()
    day2 = input().strip()
    phuphi = int(input().strip())
    id = i + 1
    my_list.append(KhachHang("KH%02d"%id, ten, phong, day1, day2, phuphi))

for i in my_list:
    i.xuli()

my_list.sort(key = lambda x: x.chiphi, reverse=True)

for i in my_list:
    print(i)