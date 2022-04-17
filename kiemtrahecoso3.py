t = int(input())

while t > 0:
    str = input()
    flag = True
    for i in range(0, len(str)):
        if (str[i] != "1" and str[i] != "2") and str[i] != "0":
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
    t -= 1

