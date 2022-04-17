t = int(input())

while t > 0:
    a, b =[int(i) for i in input().split()]
    m_list =[1, 1]
    s_list=[]
    j = 0
    k = 1
    while j < b-1:
        m_list.append(m_list[j] + m_list[k])
        j += 1
        k += 1
    s =""
    for i in range(a, b+1):
        s_list.append(m_list[i-1])

    print(*s_list)


    t -= 1