t = int(input())

while t > 0:
    num = input()
    if num[0] == num[len(num)-1]:
        print("YES")
    else:
        print("NO")
    t -= 1