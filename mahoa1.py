 # co 3 truong hop
 # 1 la cac so ma i + 1 khong phai la so cuoi cung
 # thi no se co 2 th binh thuong la giong va khong giong

# t = int(input())
# while t > 0:
#     code = input()
#     length = len(code)
#     string =""
#     count = 1
#     for i in range(0, length - 1):
#         if code[i] == code[i+1]:
#             count += 1
#         elif code[i] != code[i + 1]:
#             string += str(count) + code[i]
#             count = 1
#         if code[i] != code[i+1] and i + 1 == length - 1:
#             string += "1" + code[i + 1]
#         elif code[i] == code[i + 1] and i + 1 == length - 1:
#             string += str(count) +code[i + 1]
#     print(string)
#     t -= 1


t = int(input())

while t > 0:
    code = input()
    code +=" "
    count =1
    for i in range( len(code)-1):
        if code[i] != code[i+1]:
            print(str(count)+ code[i],end="")
            count = 1
        else:
            count+=1
    print("\n")

    t -= 1



