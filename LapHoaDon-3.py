class HoaDon:
    def __init__(self, id, ten, sl, gia, ck):
        self.id = id
        self.ten = ten
        self.sl = sl
        self.gia = gia
        self.ck = ck
        self.tongtien = self.sl * self.gia - self.ck

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + '%.0f'%self.sl + ' ' + '%.0f'%self.gia + ' ' + '%.0f'%self.ck + ' ' + '%.0f' %self.tongtien



my_list = []
for i in range(int(input())):
    id = input()
    ten = input()
    sl = int(input())
    gia = int(input())
    ck = int(input())
    my_list.append(HoaDon(id, ten, sl, gia, ck))

ans = sorted(my_list, key =lambda x : x.tongtien, reverse= True)
for i in ans:
    print(i)



