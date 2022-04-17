def sum10(n):
    sum = 0
    while n > 0:
        ans = n % 10
        sum += ans
        n = n / 10
        n = int(n)
    if sum % 10 == 0:
        return True
    else:
        return False

def distance2(n):
    ans1 = n % 10
    n /= 10
    n = int(n)
    while n > 0:
        ans2 = n % 10
        if ans1 != ans2 + 2 and ans1 != ans2 - 2:
            return False
        ans1 = ans2
        n /= 10
        n = int(n)
    return True


t = int(input())
while t > 0:
    num = int(input())
    if sum10(num) and distance2(num):
        print("YES")
    else:
        print("NO")
    t -= 1

