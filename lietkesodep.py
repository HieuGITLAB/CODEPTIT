#TLE
def tn(n):
    for i in range(len(n)):
        if n[i] != n[len(n) - i -1] or int(n[i]) % 2 != 0:
            return False
    return True
def check(n):
    num_list =[]
    for i in range(len(n)):
        num_list.append(n[i])
    k = set(num_list)
    if len(k) % 2 == 0:
        return False
    return True

t = int(input())

while t > 0:
    n = int(input())
    for i in range(22, n,2):
        if check(str(i)) and tn(str(i)):
            print(i, end=" ")
    print("\n")
    t -= 1