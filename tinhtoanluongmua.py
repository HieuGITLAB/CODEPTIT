# class Calculator():
#     def __init__(self, name, time1, time2, luongmua):
#         self.name = name
#         self.luongmua = luongmua
#         self.batdau = time1.split(":")
#         self.ketthuc = time2.split(":")
#         self.time1 = int(self.batdau[0]) * 60 + int(self.batdau[1])
#         self.time2 = int(self.ketthuc[0]) * 60 + int(self.ketthuc[1])
#
#     def subtime(self):
#         self.time3 = self.time2 - self.time1
#         return "%.2f"%(self.luongmua / self.time3)
#
# t = int(input())
# dicts = {}
# while t > 0:
#     name = input()
#     time1 = input()
#     time2 = input()
#     luongmua = int(input())
#     t1 = Calculator(name, time1, time2, luongmua)
#     if t1.name in dicts:
#         dicts[t1.name] += t1.subtime()
#     else:
#         dicts.setdefault(t1.name, t1.subtime())
#
#     t -= 1
# l1 = list(dicts.keys())
# l2 = list(dicts.values())
# for i in range(len(l1)):
#     if i + 1 < 10:
#         print(f"T0{i+1} {l1[i]} {l2[i]}")
#     else:
#         print(f"T{i+1} {l1[i]} {l2[i]}")

class TramDo():
    def __init__(self, ten, thoigian, id, luongmua):
        self.ten = ten
        self.id = id
        self.thoigian = thoigian
        self.luongmua = luongmua
        self.tb = 0

    def congdon(self, thoigian, luongmua):
        self.thoigian += thoigian
        self.luongmua += luongmua

    def tinh(self):
        self.tb = round(self.luongmua*60 / self.thoigian, 2)

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + ('%.2f'%self.tb)


my_list = []
for i in range(int(input())):
    ten = input()
    t1 = input().split(":")
    t2 = input().split(":")
    thoigian = int(t2[0]) * 60 + int(t2[1]) - int(t1[0]) * 60 - int(t1[1])
    luongmua = int(input())
    id = i + 1
    check = False
    for j in my_list:
        if ten == j.ten:
            j.congdon(thoigian, luongmua)
            check = True
            break
    if not check:
        my_list.append(TramDo(ten, thoigian, 'T%02d'%id, luongmua))

for i in my_list:
    i.tinh()
    print(i)






