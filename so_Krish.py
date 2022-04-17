import math
def factorial(n):
    return math.factorial(n)

t = int(input())

while t > 0:
    num = input()
    sum = 0
    for i in range(0, len(num)):
        sum += factorial(int(num[i]))
    if sum == int(num):
        print("Yes")
    else:
        print("No")

    t -= 1