import math


def snt(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


t = int(input())

while t > 0:
    num = input()
    sum = 0
    flag = True
    for i in range(0, len(num)):
        sum += int(num[i])
        if int(num[i]) % 2 == 0 and i % 2 != 0:
            flag = False
        elif  int(num[i]) % 2 != 0 and i % 2 == 0:
            flag = False
    if flag and snt(sum):
        print("YES")
    else:
        print("NO")
    t -= 1