def tichchuso(n):
    mul = 1
    for i in range(len(n)):
        mul *= int(n[i])
    return mul
t = int(input())

while t > 0:
    n = int(input())
    a = list(input().split())
    sorted_sum = []
    b = []
    e =[]
    for i in a:
        e.append(int(i))
    a.clear()
    e = sorted(e)
    for i in e:
        a.append(str(i))
    for i in a:
        b.append(i)
        b.append(tichchuso(i))
        sorted_sum.append(b[-1])
    sorted_sum = sorted(sorted_sum)
    ans = []
    for i in range(len(sorted_sum)):
        ans.append(b[b.index(sorted_sum[i])-1])
        b.remove(sorted_sum[i])
    print(*ans,end="")
    print("\n")
    t -= 1