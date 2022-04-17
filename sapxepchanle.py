n = int(input())
a = []
while n > 0:
    b = list(input().split())
    a.append(b)
    n -= 1


mark = []
int_list = []
for i in a:
    int_list.append(int(i))
even_list = []
odd_list = []
for i in range(n):
    if int_list[i] % 2 ==0:
        mark.append(0)
        even_list.append(int_list[i])
    else:
        mark.append(1)
        odd_list.append(int_list[i])
odd_list = sorted(odd_list)
even_list = sorted(even_list,reverse=True)
ans =[]
for i in range(n):
    if mark[i] == 0:
        ans.append(even_list[-1])
        even_list.pop()
    else:
        ans.append(odd_list[-1])
        odd_list.pop()

print(*ans, end="")
