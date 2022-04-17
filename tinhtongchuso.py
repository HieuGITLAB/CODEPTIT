t = int(input())

while t > 0:
    t -= 1
    s1 = list(input())
    sum = 0
    s1 = sorted(s1)
    count = 0
    for i in range(len(s1)):
        if ord(s1[i]) >= 48 and ord(s1[i]) <= 57:
            sum += int(s1[i])
            count += 1
    print(*s1[count:len(s1)],sum,sep="")
