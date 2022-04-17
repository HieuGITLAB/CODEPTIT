n = int(input())
a=list(input().split())
count = 0
for index in range(n-1):
    for j  in range(index+1,n):
        if int(a[index])> int(a[j]):
            count+=1
print(count)

