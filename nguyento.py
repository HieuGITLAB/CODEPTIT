def snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ucln(a, b):
    while b != 0:
        x = a % b
        a, b = b, x
    return a

t = int(input())
while t > 0:
    num = int(input())
    count  = 0
    for i in range(1, num):
        if ucln(num, i) == 1:
            count += 1
    if snt(count):
        print("YES")
    else:
        print("NO")
    t -= 1
