n = int(input())
a = list(input().split())
count = 0
flag = n - 1
for i in range(n-1):
    if i == n -1:
        break
    if a[i] != a[i+1] :
        count += 1
print(count)
