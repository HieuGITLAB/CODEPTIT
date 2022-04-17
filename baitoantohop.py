# n, k = [int(i) for i in input().split()]
# a = list(input().split())
# b = []
# for item in a:
#     b. append(int(item))
# b = sorted(b)
# b = set(b)
# b = list(b)
# n = len(b)
# s = []
# for i in range(0, k):
#     s.append(b[i])
# stop = False
# while not stop:
#     i = k - 1
#     while s[i] == b[n-k+i]:
#         i -= 1
#
#     print(*s)
#     if i < 0:
#         stop = True
#         break
#     # s[i] = b[b.index(s[i]) +1]
#     # for j in range(i+1, k):
#     #     s[j] = b[b.index(s[j-1])+1]
#     for j in range(i, k):
#         if j == i:
#             s[j] = b[b.index(s[j]) + 1]  # tăng phần tử lại vị trí pos lên 1
#         else:
#             s[j] = b[b.index(s[i]) + j -i]  # cài đặt lại các phần tử theo sau


#-----------------------------------------------------------------------------------#
#This is second solution what is soluted by python itertools import combinations
n, k = [int(i) for i in input().split()]
a = list(input().split())
b =[]
for i in a:
    b.append(int(i))
c = set(sorted(b))
c = list(c)
from itertools import combinations
comb = combinations(c,k)
for i in list(comb):
    print(*i)