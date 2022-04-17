t = int(input())
my_list=[]
while t > 0:
    str = input()
    my_list.append(str)
    t -= 1
s= set(my_list)
print(len(s))