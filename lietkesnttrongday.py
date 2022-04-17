import math


def snt(n):
    if n <2:
        return False
    for i in range(2, math.floor(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


n = int(input())
a = list(input().split())
for i in range(0, len(a)):
    flag = False
    count = 0
    for j in range(i-1,-1,-1):
        if a[i] == a[j]:
            flag = True
            break
    if flag == True:
        continue
    if snt((int(a[i]))):
        count = 1
        for j in range(i+1, n):
            if a[i] == a[j]:
                count +=1
    if count != 0:
        print(a[i], count)

