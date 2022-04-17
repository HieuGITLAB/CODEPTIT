# a, K, N = [int(i) for i in input().split()]
# list1 = []
# for i in range(1, N-a+1):
#     if i <= N - a and (a + i) % K == 0:
#         list1.append(i)
# if not list1:
#     print("-1")
# else:
#     print(*list1)


#gioi vl :D
# Mindset bai nay se la t se la so dau tien cua a + b % K == 0 hay a + t % K == 0
# So tiep theo de a + b % K == 0 cua b se la t + K

a, K, N = [int(i) for i in input().split()]
flag = False
t = K - a % K
for i in range(t, N-a+1,K):
    print(i, end=" ")
    flag = True
if not flag:
    print("-1")