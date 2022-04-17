def snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

t = int(input())

while t>0:
    number = input()
    sum = 0
    for i in range(0, len(number)):
        sum += int(number[i])
    if snt(sum):
        print("YES")
    else:
        print("NO")

    t -= 1