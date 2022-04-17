t = int(input())
while t > 0:
    num = input()
    check = False
    for i in range(0,len(num)):
        if num[i] != "4" and num[i] != "7":
            check = True
    if check == True:
        print("NO")
    else:
        print("YES")
    t -= 1