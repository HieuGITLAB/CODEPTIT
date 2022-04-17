# Wrong
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
    check = ""
    for i in range(len(num) - 4, len(num)):
        check += num[i]
    if snt(int(check)):
        print("YES")
    else:
        print("NO")
    t -= 1


