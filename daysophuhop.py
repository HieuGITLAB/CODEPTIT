t = int(input())

while t > 0:
    n = int(input())
    a = list(input().split())
    b = list(input().split())
    c = []
    d = []
    for item in a:
        c.append(int(item))
    for item in b:
        d.append(int(item))
    a = sorted(c)
    b = sorted(d)
    flag = True
    for i in range(n):
        if a[i] > b[i]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")

    t -= 1