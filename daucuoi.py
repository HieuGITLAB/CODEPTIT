t = int(input())
while t > 0:
    num = input()
    length = len(num)
    f_num = num[0] + num[1]
    l_num = num[length - 2] + num[length - 1]
    if f_num == l_num:
        print("YES")
    else:
        print("NO")
    t -= 1