# t = int(input())
#
# while t > 0:
#     num = input()
#     sum = 0
#     for i in range(0, len(num)):
#         sum += int(num[i])
#     mylist = list(str(sum))
#     r_list = mylist[:]
#     r_list.reverse()
#     for i in r_list:
#         if i == "0":
#             r_list.remove("0")
#     if mylist == r_list and sum % 10 != 0 and sum > 0:
#         print("YES")
#     else: print("NO")
#
#
#
#     t -= 1

def stn(n):
    for i in range(0, len(n)):
        if n[i] != n[len(n) -1-i]:
            return False
    return True

t = int(input())

while t > 0:
    n = input()
    sum = 0
    for i in range(0, len(n)):
        sum += int(n[i])
    if stn(str(sum)) and sum > 10:
        print("YES")
    else:
        print("NO")
    t -= 1