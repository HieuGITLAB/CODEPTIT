t = int(input())

while t > 0:
    str = input()
    mylist = list(str)
    r_list = list(str)
    r_list.reverse()
    flag = True
    for i in range(1,len(mylist)):
        if abs(ord(mylist[i]) - ord(mylist[i-1])) != abs(ord(r_list[i]) - ord(r_list[i-1])):
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
    t -= 1