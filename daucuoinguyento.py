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
    num1 = num[0] + num[1] + num[2]
    num2 = num[len(num)-3] + num[len(num)-2] + num[len(num)-1]
    if snt(int(num1)) and snt(int(num2)):
        print("YES")
    else:
        print("NO")

    t -= 1