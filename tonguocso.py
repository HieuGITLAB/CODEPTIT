t = int(input())
sum = 0
while t > 0:
    n = int(input())
    for i in range(2, n+1):
        while n % i == 0:
            sum += i
            n = n / i
            n = int(n)
    t -= 1
print(sum)
