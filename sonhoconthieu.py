n = int(input())
a = list(input().split())
b = []
for item in a:
    b.append(int(item))
b = sorted(b)
flag = True
for i in range(len(b)-1):
    if b[i+1] - b[i] != 1:
        print(b[i]+1)
        flag = False
        break
if flag:
    print(b[len(b)-1]+1)
