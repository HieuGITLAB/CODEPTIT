import datetime
class LichThi():
    def __init__(self, ma, ten, id, ngay, gio, nhom):
        self.ma = ma
        self.ten =ten
        self.id = id
        self.ngay = datetime.datetime.strptime(ngay, "%d/%m/%Y").date()
        self.gio = gio
        self.nhom = nhom


    def __str__(self):
        return self.id + " " + self.ma + " " + self.ten + " " + str(self.ngay) + " " + self.gio + " " + self.nhom



my_list = []
dicts = {}
n, m = [int(i) for i in input().split()]
for i in range(0, n):
    ma = input()
    ten = input()
    dicts.setdefault(ma, ten)


for i in range(0, m):
    id = i + 1
    ma2, ngay, gio, nhom = [str(i) for i in input().split()]
    for k in dicts:
        if k == ma2:
            my_list.append(LichThi(ma2, dicts[k], "T%03d"%id, ngay, gio, nhom))

ans = sorted(my_list, key=lambda x:(x.ngay, x.gio, x.ma))
for i in ans:
    i.ngay = i.ngay.strftime("%d/%m/%Y")
    print(i)
#
#
# from datetime import date
# my_list =[]
# day = date(2022, 12, 3)
# day2 = date(2022,12,14)
# day3 = date(2023,2,23)
# my_list.append(day)
# my_list.append(day2)
# my_list.append(day3)
# my_list.sort(reverse=True)
# for i in my_list:
#     print(i)
