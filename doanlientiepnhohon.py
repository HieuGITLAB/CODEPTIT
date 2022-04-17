t = int(input())

while t > 0:
    n = int(input())
    a = list(input().split())
    b = []
    ans = []
    for i in a:
        b.append(int(i))
    for i in range(n):
        count = 1
        for j in range(i-1, 0, -1):
            if b[j] <= b[i]:
                count += 1
            else:
                break
        ans.append(count)
    print(*ans)
    t -= 1