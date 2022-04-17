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
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_x(n):
    sum = 0
    while n > 0:
        a = n % 10
        sum += a
        n /= 10
        n = int(n)
    return sum

while t > 0:
    num, num2 = [int(i) for i in input().split()]
    if snt(sum_x(ucln(num, num2))):
        print("YES")
    else:
        print("NO")
    t -= 1