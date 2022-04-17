def _check(n):
    if n < 2:
        return False
    if n > 3:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True
n,m=input().split()
n=int(n)
m=int(m)
list=[]
for i in range(n):
    arr=[int(i) for i in input().split()]
    list.append(arr)
for i in range(n):
    for j in range(m):
        if _check(list[i][j]):
            list[i][j]=1
        else:
            list[i][j]=0
for i in range(n):
    for j in range(m):
        print(list[i][j],end=" ")
    print()