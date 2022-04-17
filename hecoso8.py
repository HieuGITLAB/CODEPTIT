num = 0
s = input()
if len(s) % 3 != 0:
    k = 3 - (len(s) % 3)
    s = "0" * k + s
hat = 0
ans = []
for i in range(len(s)-1, -1, -1):
    num += int(s[i]) * (2**hat)
    hat += 1
    if i % 3 == 0:
        ans.insert(0,num)
        hat = 0
        num = 0
print(*ans, sep="")


