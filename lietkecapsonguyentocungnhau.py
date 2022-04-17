def ucln(a, b):
    while b != 0:
        x = a % b
        a, b = b, x
    return a

n = int(input())
a = list(input().split())
b = []
for item in a:
    b.append(int(item))
b = sorted(b)
for i in range(n -1):
    for j in range(i+1, n):
        if ucln(b[i], b[j]) == 1:
            print(b[i], b[j])

