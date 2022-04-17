t = int(input())

while t > 0:
    num = input()
    sum = 0
    multi = 1
    for i in range(0, len(num), 2):
        sum += int(num[i])
    count = 0
    for i in range(1, len(num), 2):
        if num[i] == "0":
            continue
        else:
            multi *= int(num[i])
            count += 1
    if count != 0:
        print(sum, multi)
    else:
        print(sum, "0")


    t -= 1