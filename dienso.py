t = int(input())

while t > 0:
    n = int(input())
    index = list(input().split())
    index = set(index)
    b = list(index)
    a = []
    for i in b:
        a.append(int(i))
    a.sort()
    ans2 = []
    for i in range(0, len(a)-1):
        ans = int(a[i+1]) - int(a[i])
        if ans > 1:
            for j in range(1, ans):
                ans2.append(int(a[i]) + j)
    print(len(ans2))

    t -= 1