from datetime import datetime
class ThiSinh():
    def __init__(self, ten, tp, id, t1):
        self.ten = ten
        self.tp = tp
        self.id = id
        self.t1 = datetime.strptime(t1,"%H:%M")
        self.t2 = datetime.strptime("6:00","%H:%M")
        self.vt = 0

    def calcu(self):
        time = list(str(self.t1 - self.t2).split(":"))
        self.vt = 120/(int(time[0]) + float(int(time[1])/60))
        self.vt = round(self.vt)

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + self.tp + ' ' + '%.0f'%self.vt + ' ' + "Km/h"

my_list = []
for i in range(int(input())):
    ten = input()
    tp = input()
    xuli = tp.title() + ten.title()
    id = ""
    for j in range(len(xuli)):
        if xuli[j].isupper():
            id += xuli[j]
    t1 = input()
    my_list.append(ThiSinh(ten, tp, id, t1))

for i in my_list:
    i.calcu()
my_list.sort(key = lambda x: x.vt, reverse=True)
for i in my_list:
    print(i)

# 4
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45
# Tran Vu Hien
# Long An
# 7:00