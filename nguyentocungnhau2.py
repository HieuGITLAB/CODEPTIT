def ucln(a,b):
    while b!= 0:
        x = a % b
        a, b =  b, x
    return a

n = int(input())
a = list(input().split())
b =  []
for item in a:
    b.append(int(item))
b = sorted(b)
for i in range(0, len(b)):
    for j in range(i+1, len(b)):
        if ucln(b[i], b[j]) == 1:
            print(f"{b[i]} {b[j]}")



