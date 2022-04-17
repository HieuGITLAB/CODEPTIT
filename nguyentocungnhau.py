import math

def ucln(a, b):
    while(b != 0):
        x = a % b
        a, b = b, x
    return a
my_list = []
N, K = [int(i) for i in input().split()]
count = 0
for i in range(int(math.pow(10,K-1)), int(math.pow(10, K))):
    if ucln(N, int(i)) == 1:
        my_list.append(i)
        count += 1
    if count % 10 == 0 and count != 0:
        print(*my_list)
        my_list =[]
        count = 0
print(*my_list)
