def ucln(a, b):
    while b != 0:
        x = a % b
        a, b = b, x
    return a

t = int(input())

while t > 0:
    n1 = int(input())
    n2 = int(input())
    print(ucln(n1, n2))
    t -= 1