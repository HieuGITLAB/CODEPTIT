# import re
# t = int(input())
#
# while t > 0:
#     n = int(input())
#     a = list(input().split())
#     b = []
#     for item in a:
#         b.append(int(item))
#     best_value = []
#     best_key =[int(n/2)]
#     b = sorted(b)
#     count = 1
#     for i in range(0, len(b)-1):
#         if b[i] == b[i+1]:
#             count += 1
#         else:
#             count = 1
#         if count > best_key[0]:
#             best_key[0] = count
#             print(best_key[0])
#             best_value.append(b[i])
#     if best_value:
#         print(best_value[0])
#     else:
#         print("NO")
#
#     t -= 1
t = int(input())
while t > 0:
    n = int(input())
    day = input().split()
    day = list(map(lambda x: int(x) if x.isdigit() else 0, day))
    answer = []
    for i in day:
        if day.count(i) > n/2 : 
              answer.append(i)
              break
    if len(answer) == 0:
        print("NO")
    else:
        print(answer[0])
    t -= 1