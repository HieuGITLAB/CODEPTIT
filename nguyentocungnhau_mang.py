def ucln(a, b):
    while b != 0:
        x = a % b
        a, b = b, x
    return a

n = int(input())
a = list(input().split())
for item in a:
    item = int(item)
a.sort()
print(a)
for i in range(n):
    for j in range(i +1, n):
        if a[i] == a[j]:
            continue
        if ucln(int(a[i]), int(a[j])) == 1:
            print(a[i], a[j])


