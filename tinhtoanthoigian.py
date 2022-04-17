class NguoiChoi():
    def __init__(self, id, ten, tb):
        self.id = id
        self.ten = ten
        self.tb = tb
        self.gio = 0
        self.phut = 0

    def tinh(self):
        self.gio = self.tb // 60
        self.phut = self.tb - self.gio*60

    def __str__(self):
        return self.id + " " + self.ten + " " + ('%.0f'%self.gio) + " gio " + ('%.0f'%self.phut) + " phut"

my_list = []
for i in range(int(input())):
    id = input()
    ten = input()
    t1 = input().split(":")
    t2 = input().split(":")
    tb = int(t2[0]) * 60 + int(t2[1]) - int(t1[0]) * 60 - int(t1[1])
    my_list.append(NguoiChoi(id, ten, tb))

for i in my_list:
    i.tinh()

ans = sorted(my_list, key= lambda x : x.tb, reverse=True)
for i in ans:
    print(i)
