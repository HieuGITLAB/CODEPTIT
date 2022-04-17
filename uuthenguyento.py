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
    count = 0
    for i in range(0, len(num)):
        if snt(int(num[i])):
            count += 1
    if 2 * count > len(num) and snt(len(num)):
        print("YES")
    else:
        print("NO")
    t -= 1
