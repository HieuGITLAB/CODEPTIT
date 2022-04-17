# # dau tien tim so thu 1
# # tim so thu 2 xem co > 4 khong thi up so thu 1 += 1 va nhan voi power
# # neu so thu 2 = 4 va cac so con lai lon hon or = 4 va so cuoi cung > 4 thi cx up
# def count_num(num):
#     count = 0
#     while num >= 1:
#         num /= 10
#         count += 1
#     return count
#
# def power(num):
#     pow_num = 10 ** (count_num(num) -1)
#     return pow_num
#
# def check(num):
#     a = num % 10
#     num /= 10
#     if a < 5:
#         return False
#     while num >= 1:
#         a = num % 10
#         if a < 4:
#             return False
#         num /= 10
#     return True
#
# t = int(input())
# while t > 0:
#     num = int(input())
#     if num <= 10:
#         print(num)
#     else:
#         f_num = int(num / power(num))
#         s_num = int((num / (power(num)/ 10)) % 10)
#         remaindder = num % (power(num) / 10)
#         if s_num < 5 and remaindder == 0:
#             num = f_num * power(num)
#         if s_num >= 5:
#             f_num += 1
#             num = f_num * power(num)
#         elif s_num == 4 and check(remaindder) == True:
#             f_num += 1
#             num = f_num * power(num)
#         else:
#             num = f_num * power(num)
#         print(num)
#     t -= 1


#------------------------------------------------
#De vl ma khong nghi duoc :D
# mindset no se la neu n[i] >= 5 thi n[i-1] +=1
#sau do n[i] = 0
t = int(input())
while t > 0:
    n = [int(i) for i  in input()]
    for i in range(len(n) - 1, 0, -1):
        if n[i] >= 5:
            n[i-1] +=1
        n[i] = 0
    print(*n, sep="")
    t -= 1


