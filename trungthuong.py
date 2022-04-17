t = int(input())

while t > 0:
    x = int(input())
    count = 0
    my_list = []
    num = []
    while x > 0:
        n = int(input())
        my_list.append(n)
        tmp = 0
        tmp += my_list.count(n)
        if tmp > count:
            count = tmp
            num.clear()
        if tmp >= count:
            num.append(n)
        x -=1
        if x == 0:
            print(min(num))
    t -= 1