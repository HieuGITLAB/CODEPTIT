class HoaDon():
    def __init__(self, ten, id, khoiluong):
        self.ten = ten
        self.khoiluong = khoiluong
        self.tong = 0
        self.id = id

    def tinh(self):
        if self.khoiluong <= 50:
            self.tong = self.khoiluong*100 * 1.02
            self.tong = round(self.tong, 0)
        elif self.khoiluong <= 100:
            self.tong = ((50 * 100) + (self.khoiluong - 50) * 150) * 1.03
            self.tong = round(self.tong, 0)
        else:
            self.tong = ((50 * 100) + (50 * 150) + (self.khoiluong - 100) * 200) * 1.05
            self.tong = round(self.tong, 0)

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + ('%.0f'%self.tong)

my_list = []
for i in range(int(input())):
    ten = input()
    l1 = int(input())
    l2 = int(input())
    khoiluong = l2 - l1
    id = i + 1
    my_list.append(HoaDon(ten, 'KH%02d'%id, khoiluong))

for i in my_list:
    i.tinh()

ans = sorted(my_list, key= lambda  x: x.tong, reverse= True)
for i in ans:
    print(i)

