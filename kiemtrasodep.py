t = int(input())
while t > 0:
    num = input()
    length = len(num)
    flag = True
    for i in range(0, length, 2):
        if num[i] != num[0]:
            flag = False
            break
    for i in range(1, length, 2):
        if num[i] != num[1]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
    t -= 1