t = int(input())

while t > 0:
    my_list = []
    mes = input()
    s = ""
    for i in range(len(mes)):
        if ord(mes[i]) >= ord("0") and ord(mes[i]) <= ord("9"):
            s += mes[i]
        else:
            if s != "":
                my_list.append(int(s))
                s = ""
    if s != "":
        my_list.append(int(s))
    print(max(my_list))


    t -= 1