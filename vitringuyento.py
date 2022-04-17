import math
#kiem tra xem phan tu i co trong day khong: if i in list :))


def snt(n):
    if n < 2:
        return False
    for i in range(2,math.floor(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

t = int(input())

while t > 0:
    flag = True
    flag2 = True
    num = input()
    for i in range(0, len(num)):
        if snt(int(num[i])) == False and snt(i):
            flag = False
        if snt(int(num[i])) and snt(i) == False:
            flag2 = False
    if flag and flag2:
        print("YES")
    else:
        print("NO")
    t -= 1