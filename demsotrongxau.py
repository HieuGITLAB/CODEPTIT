t = int(input())

while t > 0:
    s = input()
    N = input()
    count = 0
    d = 0
    length = len(N)
    for i in range(0, len(s)):
        if i < d:
            continue
        flag = True
        if s[i] == N[0]:
            k = i
            for j in range(1, len(N)):
                if k == len(s) -1:
                    break
                k += 1
                if s[k] != N[j]:
                    flag = False
                    break

        if flag == True and s[i] == N[0] and i != len(s) -1:
            count += 1
            d = i+ length
        else:
            d = 1

    print(count)

    t -= 1
    