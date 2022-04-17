n=int(input())
a=[]
for i in range(n):
    b=[int(i) for i in input().split()]
    a.append(b)
k=int(input())
tongtren=0
tongduoi=0
for i in range(n):
    for j in range(i+1,n):
        tongtren+=a[i][j]
for i in range(1,n):
    for j in range(i):
        tongduoi+=a[i][j]
m=abs(tongtren-tongduoi)
if m<=k:print("YES")
else :print("NO")
print(m)