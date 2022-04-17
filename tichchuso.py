t = int(input())

while t > 0:
    multi = 1
    num = input()
    for i in range(0, len(num)):
        if num[i] == "0":
            pass
        else:
            multi *= int(num[i])

    print(multi)
    t -= 1

