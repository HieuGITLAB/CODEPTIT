import math


def snt(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n) +1 )):
        if n % i == 0:
            return False
    return True

t = int(input())

while t > 0:
    number = input()
    length = len(number)
    count = 0
    for i in range(0, len(number)):
        if snt(int(number[i])):
            count += 1
        if count > length - count:
            break
    if snt(length) and count > length - count:
        print("YES")
    else:
        print("NO")

    t -= 1