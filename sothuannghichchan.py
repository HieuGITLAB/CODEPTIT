def tn(n):
    my_list = list(n)
    r_list = list(n)
    r_list.reverse()
    if my_list == r_list:
        return True
    return False

def check(n):
    for i in range(0, len(n)):
        if int(n[i]) % 2 != 0:
            return False
    return True

t = int(input())

while t > 0:
    num = int(input())
    m_list =[]
    for i in range(1, num):
        if tn(str(i)) and check(str(i)) and len(str(i)) % 2 == 0:
            m_list.append(i)
    print(*m_list)
    t -= 1
