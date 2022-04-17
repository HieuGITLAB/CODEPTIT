t = int(input())

while t > 0:
    n, d = [int(i) for i in input().split()]
    a = list(input().split())
    while d > 0:
        mark = a[0]
        del a[0]
        a.append(mark)
        d -= 1
    print(*a)
    t -= 1