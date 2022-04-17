import math


def snt(n):
    if n <2:
        return False
    for i in range(2, math.floor(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

N, X = [int(i) for i in input().split()]
snt_list = [X]
mark = 1
for i in range(2, N*N,1):
    if snt(i):
        mark += 1
        snt_list.append(i)
    if mark == N+1:
        break
for i in range(1,N+1):
    snt_list[i] += snt_list[i-1]
print(*snt_list)



