t = 1
while True:
    n = int(input())
    if n == 0:
        break
    num_list = []
    sort_list = []
    while n > 0:
        num = input()
        num = num.lstrip('0')
        num_list.append(num)
        n -= 1
    num_list = sorted(num_list)
    for i in num_list:
        sort_list.append(int(i))
    sort_list = sorted(sort_list)
    if sort_list[0] == sort_list[-1]:
        print("BANG NHAU")
    else:
        print(sort_list[0], sort_list[-1])
