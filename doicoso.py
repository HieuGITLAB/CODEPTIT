t = int(input())

while t > 0:
    n, k = [int(i) for i in input().split()]
    ans1 =[]
    while True:
        ans = n %  k
        if ans < 10:
            ans1.append(ans)
        else:
            ans1.append(chr(ans + 55))
        n = n // k
        if n == 0:
            break
    ans1.reverse()
    print(*ans1, sep="")





    t -= 1