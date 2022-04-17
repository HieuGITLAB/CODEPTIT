t = int(input())
while t > 0:
    string1 = input()
    string2 = ""
    for i in range(len(string1) - 1, -1, -1):
        string2 += string1[i]
    check = True
    for i in range(1, len(string1)):
        if abs(ord(string1[i]) - ord(string1[i-1])) != abs(ord(string2[i]) - ord(string2[i-1])):
            check = False
        if check == False:
            print("NO")
            break
    if check == True:
        print("YES")
    t -= 1