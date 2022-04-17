#Wrong
# t = int(input())
#
# while t > 0:
#     n = input()
#     d = 0
#     my_list = []
#     for i in range(0, len(n)):
#         if i <= d and i != 0:
#             continue
#         str = ""
#         while n[i] >= "0" and n[i] <= "9":
#             str += n[i]
#             if i == len(n) - 1 :
#                 break
#             i += 1
#             d = i
#         if str != "":
#             my_list.append(int(str))
#     print(my_list)
#     print(min(my_list))
#     t -= 1


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
    print(min(my_list))


    t -= 1