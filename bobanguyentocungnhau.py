import math

a, b = [int(i) for i in input().split()]

def ucln(a, b):
    while b != 0:
        x = a % b
        a, b = b, x
    return a
# def snt(n):
#     if n < 2:
#         return False
#     for i in range(2, math.floor(math.sqrt(n)+1)):
#         if n % i == 0:
#             return False
#     return True
#
# snt_list = []
# for i in range(a, b +1):
#     if snt(i):
#         snt_list.append(i)
#
# for i in range(a, b +1):
#     if i not in snt_list:
#         for j in range(i+1, b +1):
#             if j not in snt_list and ucln(i,j) == 1:
#                 for item in snt_list:
#                     print(f"({i}, {j}, {item}  1)")
#                 if ucln(item, j) ==1:
#                     print(f"({i}, {item}, {j}  1)")
#             if j in snt_list:
#                 for item in snt_list:
#                     if j >= item:
#                         continue
#                     print(f"({i}, {j}, {item} 2)")
#     if i in snt_list:
#         for j in range(i+1, b+1):
#             for item in snt_list:
#                 if i >= item:
#                     continue
#                 if j not in snt_list and j < item:
#                     print(f"({i}, {j}, {item}  3)")
#                 elif j not in snt_list and j > item:
#                     print(f"({i}, {item}, {j}  4)")
for i in range(a, b-1):
    for j in range(i+1, b):
        if ucln(i, j) ==1:
            for k in range(j+1, b+1):
                if ucln(i,k) == 1 and ucln(j,k) == 1:
                    print(f"({i}, {j}, {k})")



