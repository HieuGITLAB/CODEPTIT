# a = list(input().split())
# c =[]
# for item in a:
#     c.append(int(item)%42)
# b = set(c)
# print(len(b))
# test=10
# while test>0:
#     data=input()
#     base=data.split()
#
#     test -=len(base)

t = []
while len(t) < 10:
  n = [int(i) for i in input().split()]
  t += n
  a = []
  for i in t:
        a.append(i % 42)
print(len(set(a)))