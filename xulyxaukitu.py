s1 = input().lower()
s2 = input().lower()
head = 0
tail = 0
s = set()
for i in range(0, len(s1)):
    if s1[i] == " ":
        s.add(s1[head:i])
        head = i + 1
s.add(s1[head:len(s1)])

st1 = s.copy()
st2 = set()
head = 0
for i in range(0, len(s2)):
    if s2[i] == " ":
        s.add(s2[head:i])
        st2.add(s2[head:i])
        head = i + 1
s.add(s2[head:len(s2)])
st2.add(s2[head:len(s2)])
s = sorted(list(s))
st1 = sorted(list(st1))
st2 = sorted(list(st2))
ans = []

print(*s)
for i in st1:
    for j in st2:
        if i == j:
            ans.append(i)
print(*ans)

