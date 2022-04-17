t =int(input())
while t > 0:
    code = input()
    code1 = ""
    for i in range(0,len(code), 2):
        code1 += code[i] * int(code[i+1])

    print(code1)
    t -= 1


