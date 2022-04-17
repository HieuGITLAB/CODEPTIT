t = int(input())

while t > 0:
    num1 = input()
    flag = True
    for index in range(len(num1)-1):
        if num1[index+1] < num1[index]:
            flag = False
            break
    if flag == True:
        print("YES")
    else:
        print("NO")
    t-=1
