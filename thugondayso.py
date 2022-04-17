n = int(input())
a = list(input().split())
sum = 0
for i in range(0, len(a)):
    sum = a[i] + a[i+1]
    if sum % 2 == 0:


