t = 0
a = int(input())
while a != t:
    count = 1
    while a != 1:
        if a % 2 == 0:
            a = int(a/2)
            count +=1
        else:
            a = int(a*3 +1)
            count +=1
    print(count)
    a = int(input())
