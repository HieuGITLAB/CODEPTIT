t = int(input())

while t > 0:
    num = input()
    sum = 0
    multi = 1
    for i in range(0, len(num), 2):
        if num[i] == "0":
            continue
        multi *= int(num[i])
    for i in range(1, len(num), 2):
            sum += int(num[i])
    print(multi, sum)


    t -= 1