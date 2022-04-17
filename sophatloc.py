t = int(input())
while t > 0:
   num = input()
   length = len(num)
   if num[length-1] == "6" and num[length-2] == "8":
       print("YES")
   else:
       print("NO")
   t -= 1