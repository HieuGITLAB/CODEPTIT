def check(n):
    if int(len(n)) % 2 == 0:
        return False
    if n[0] == n[1]:
        return False
    for i in range(0, len(n)-1, 2):
        if n[i] != n[i+2]:
            return False
    return True

t = int(input())

while t > 0:
    n = str(input())
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1
