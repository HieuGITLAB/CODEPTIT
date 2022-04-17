import math

t = int(input())

def ucln(a, b):
    while(b != 0):
        x = a % b
        a, b = b, x
    return a

def snt(n):
    if n < 2:
        return False
    for i in range(2, math.sqrt(n)):
        if n % i == 0:
            return False
    return True


while t > 0:
    num = input()
    num2 = ""
    for i in range(len(num) - 1, -1, -1):
        num2 += num[i]
    if ucln(int(num), int(num2)) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1