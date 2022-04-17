# s = input()
# s1 = [s]
# print(s1)
# n = len(s)
# tmp = 0
# mark =[ tmp for i in range(0, 20)]
# print(mark)
#
# def Try(k):
#     for i in range(0, n):
#         if not mark[i]:
#             s1[k] = i
#             mark[i] = 1
#             if k == n -1:
#                 print(s1)
#             else:
#                 Try(k = k+1)
#             mark[i] = 0
# Try(k =0)

from itertools import permutations
s = input()
a = []
for i in range(len(s)):
    a.append(s[i])
perm = permutations(a)
for i in list(perm):
    print(*i,sep="")
